from emerson import Remote

if __name__ == "__main__":
    with Remote(f"http://localhost:10314").connect() as connection:
        project_name = "arduino-uno-r3"
        session_id = "arduino-ide-session"
        connection.stop_project(session_id)
        connection.run_session(project_name, session_id)