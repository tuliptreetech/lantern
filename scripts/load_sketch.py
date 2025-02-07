from emerson import Remote
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.WARNING)

if __name__ == "__main__":
    with Remote(f"http://localhost:10314").connect() as connection:
        project_name = "arduino-uno-r3"
        session_id = "arduino-ide-session"
        connection.run_session(project_name, session_id)
        connection.enable_gdb(project_name, session_id)
