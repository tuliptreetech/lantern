# Lantern
This is a set of project files for running the Lantern version of Emerson

## Install the docker images
Run the install script! It will prompt you for your license key.
```
./install
```

## Run the server
```
./server start
```

## Connect to the hardware simulator
You can then connect to the gui and the hardware simulator, http://localhost:10314

1. Start the project
2. Load the booted snapshot
3. Go
4. Using tty1, you can interact with the system
5. Any files you put in the `.share` directory will be available to the emulated machine in the `/host` directory

## Run a unit test
```
./client test <file_to_run>
```

This will run the file in the emulator, capture the output, and exit with the exit code of the supplied file. You can hook this into a testing framework.

## Examples
We have included a built version of each example in the `.share` directory which you can use out of the box. They are in the `/host` directory in the emulated machine.

To run the hello-world example, interact with tty1 and do this
```
/ # ls /host
hello        hello-fails  snake
/ # /host/hello
hello-world
/ # echo $?
0
/ # 
```

If you want to build them yourself, here's how.

### Hello World
To experiment, build our hello-world example 
```
earthly --artifact ./arm-examples+build-hello-world/hello-world `pwd`/.share/hello
```

If you don't have earthly, you'll need to cross compile the code yourself.
```
arm-linux-gnueabi-gcc -o ./.share/hello -static -march=armv4 -marm arm_examples/hello-world/main.c
```

### Hello World Fails
To experiment, build our hello-world example, this one exits with a non zero return code.
```
earthly --artifact ./arm-examples+build-hello-world-fails/hello-world-fails `pwd`/.share/hello-fails
```

If you don't have earthly, you'll need to cross compile the code yourself.
```
arm-linux-gnueabi-gcc -o ./.share/hello-fails -static -march=armv4 -marm arm_examples/hello-world/main-fails.c
```

### Terminal Snake
You can also play terminal snake! 
```
earthly --artifact ./arm-examples+build-terminal-snake/terminal-snake `pwd`/.share/snake
```

If you don't have earthly, you'll need to apply our patch (we don't provide a size of the terminal back to the server) and cross compile the code yourself.
```
wget https://github.com/tbpaolini/terminal-snake/archive/refs/heads/master.zip
unzip master.zip
patch -u terminal-snake-master/src/game_loop.c -i ./terminal-snake.patch
arm-linux-gnueabi-gcc -o ./.share/snake -static -march=armv4 -marm terminal-snake-master/src/main.c
```

You can interact with these examples through the tty1 serial device in the web gui.
