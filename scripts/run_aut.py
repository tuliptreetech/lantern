from emerson import script, PythonMachine
import asyncio, json

@script.run(host="server", port=10314, project_name="lantern")
async def take_snapshot(machine: PythonMachine):
    print(machine.get_tick_count())
    machine.load_snapshot_from_data_store("booted")
    machine.go()
    machine.send_to_broker("tty1", "\r\n".encode("utf8"))
    machine.send_to_broker("tty1", "/host/aut\r\n".encode("utf8"))
    line = ""
    while True:
        data = json.loads(await machine.await_serial_event())
        print(data)

        print(bytes(data['data']).decode("utf8"))
        line += bytes(data['data']).decode("utf8")
        if line[len(line)-1] == "\n":
            print(data['name'])
            print(line)
            print(machine.get_tick_count())
            line = ""

        if line == "/ # ":
            break

if __name__ == "__main__":
    take_snapshot()