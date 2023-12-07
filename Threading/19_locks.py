'''
- threading module provides a Lock class to deal with the race conditions.
Lock has two states:
    - Locked :
        - acquire()
            - change the state of code to locked
            - other threads have to wait until lock is
            relese by the current working thread.
            - Syntax: lock_obj.acquire([blocking=True], timeout=-1)
            timeout = Means how much time we give a thread to perform task.
            -1 timeout is thread has enough time to complete the task.
            blocking = True means thread itself release the lock.
    - Unlocked : release
'''
from threading import Lock, Thread
from time import sleep

mylock = Lock()


def task(mylock, msg):
    # output would me same but show run time error for below line
    # mylock.acquire(blocking=False)
    mylock.acquire()
    for i in range(5):
        print(msg)
    sleep(3)
    mylock.release()


t1 = Thread(target=task, args=(mylock, "Hello"))
t2 = Thread(target=task, args=(mylock, "Hi..."))
t1.start()
t2.start()
