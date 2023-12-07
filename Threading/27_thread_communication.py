'''
Three ways:
    - By creating event object
    - By creating condition object
    - By using queqe object

- using event object we can make communication between two thread only.
- in this we mantain one flag varable

Steps:
- First, we have to create an event object.
- Create two threads which will communicate.
- Put t2 thread in waiting by using wait().
- Use set() method in/after t1 threads code.

set()
- Set the flag value to true.
- If flag is True, waiting thread is awakened.

reset()
- Reset he internal flag to false.
- other thread will wait() again.

is_set()
- Return True is and only if the internal flag is true.

wait([timeout])
- Calling this function keep other thread on the wait until flag is set to True
- Default value of timeout is -1

'''
