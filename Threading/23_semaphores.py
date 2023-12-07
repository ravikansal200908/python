'''
- it help us to execute particular thread at time.
- It used to limit the access to thte shared resources with limit capacity.
- When thread aquire then counter get decrease by one
- When thread resease then counter get increase by one
- When count become zero then other thread will wait.
'''
from threading import Thread, Semaphore
from time import sleep
# from threading import BoundedSemaphore

# lck = BoundedSemaphore()
lck = Semaphore(1)  # Default value is one
# lck = Semaphore(3)  # Default value is one


def display(name: str) -> None:
    lck.acquire()
    for i in range(5):
        print("Hello ", name)
        sleep(0.5)
    lck.release()


t1 = Thread(target=display, args=('Thread-1',))
t2 = Thread(target=display, args=('Thread-2',))
t3 = Thread(target=display, args=('Thread-3',))
t4 = Thread(target=display, args=('Thread-4',))
t5 = Thread(target=display, args=('Thread-5',))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

'''
Semaphore has one issue:
- If acquire at 1 and release at more times then counter vales become different
- In such case we shoud use BoundedSemaphore
'''
