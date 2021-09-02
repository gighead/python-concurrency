## Process

- Created by the operating system to run applications and programs
- Processes can have multiple threads
- Processes have more overhead than threads as opening/closing processes takes more time
- Sharing information between processes is slower than sharing between threads as processes do not share memory space. In python they share information by pickling data structures like arrays which requires IO time.
- Two processes *can*s execute code simultaneously in the same python program


## Thread

- Threads are like mini-processes
- They exist in shared memory space and can easily access the same variables
- Two threads *cannot* execute code simultaneously in the same python program (with exceptions)
