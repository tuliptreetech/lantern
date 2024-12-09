This is a set of project files for running the Lantern project in ghcr.io/tuliptreetech/emerson/lantern:latest

To experiment, build the arm examples, then run the project

To build the hello-world example 
```
earthly --artifact ./arm-examples+build-hello-world/hello-world ./hello
```

To build the terminal-snake example 
```
earthly --artifact ./arm-examples+build-terminal-snake/terminal-snake ./snake
```

Then run emerson
```
docker compose up server
```

Conenct to the gui, http://localhost:10314

1. Start the project
2. Load the booted snapshot
2. Go
3. using tty1, you can execute the `/host/hello` example
