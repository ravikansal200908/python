'''
- Daemon threads also known as supportive threads
- Example : IDLE app
    - Thread 1 : Main Thread
    - Thread 2 : Thread for interactive shell
    - Thread 3 : Thread for editor
    - Thread 4 : Thread for python interpreter
    - Thread 5 : Thread for text highlighting
    - Thread 6 : Thread for memory management
- Thread 1-4 are Non daemon threada while Thread 5-6 are daemon threads

- Non-daemon threads
   - program will not terminate until all non-daemon threads gets completed.

- Daemon threads
    - A daemon thread is a thread which runs continuoisly in background
    and provide support to other non-daemon threads
    - When all non daemon threads get terminated, automaticall
    it also get terminated
    - It useful in monitoring, background services, or cleanup operation

- Some key point
    - To check daemon thread use t1.daemon --> True/False
    - To change daemon nature for thread t1.daemon = True
    - You can not change daemon nature of running thread
    - By default main thread is non-daemon
    - When we create a new thread daemon nature is inherited from parent thread
'''
