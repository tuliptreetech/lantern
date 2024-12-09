from emerson import Remote, Connection, Machine
import pytest, sys

@pytest.fixture
def machine():
    with Remote(f"http://server:10314").connect() as conn:
        print("[+] Listing projects:")
        for project in conn.project_list():
            print(f" * {project}")

        connected = False
        for (session, project_name) in conn.get_instance_list():
            if project_name == "lantern":
                print(f"[+] connecting to existing instance {session}")
                session_id = session
                connected = True
                break

        if not connected:
            session_id = conn.run_project("lantern")
            print(f"[+] creating a new session {session_id}")

        with conn.attach(session_id) as machine:
            yield machine
        conn.stop_project(session_id)

def test_step_some(machine: Machine):
    assert(machine.get_tick_count() == 0)
    machine.step(1)
    assert(machine.get_tick_count() == 1)

if __name__ == '__main__':
    sys.exit(pytest.main(["-x", __file__]))