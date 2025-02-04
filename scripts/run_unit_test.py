from emerson import script, PythonMachine
import asyncio, json, sys, logging

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.WARNING)

async def get_output(machine: PythonMachine, original_command: str) -> str:
    command = original_command + "\n"
    machine.send_to_broker("virtio_console_broker_0", command.encode("utf8"))

    lines = ""
    line = ""

    no_prompt_yet = True
    while no_prompt_yet:
        buffer = machine.read_serial_buffer()
        if buffer is None or buffer == "":
            await asyncio.sleep(2)
            continue

        for json_document in buffer.split('}'):
            if json_document is None or json_document == "":
                break

            json_document += '}'

            data = json.loads(json_document)
            this_packet = bytes(data['data']).decode("utf8")

            line += this_packet

            if line == "/ # ":
                no_prompt_yet = False
                break

            if line[len(line)-1] == '\n':

                if line[:len(original_command)] == original_command:
                    line = ""
                    continue
                lines += line
                line = ""
    return lines


@script.run_quietly(host="server", port=10314, project_name="armv5-virtio")
async def run_application_under_test(machine: PythonMachine):
    machine.load_snapshot_from_data_store("booted")
    machine.go()

    output_from_hello = await get_output(machine, "/host/test")
    return_code = int(await get_output(machine, "echo $?"))

    print(output_from_hello.replace("\r\n", "\n").replace("\r", ""))
    return return_code

if __name__ == "__main__":
    exit_code = run_application_under_test()
    sys.exit(exit_code)
