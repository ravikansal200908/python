'''
Threading identity number
- Thread Identifier
    - It's provided by process.
    - Assigned by python interpreter.
    - Read-only +ve integer and unique in process.
    - Assigned after starting thread.
    - Stored in an instance variable :- ident
- Native Identifier
    - It's provided by OS.
    - propert name :- native_id
    - Note: Generally, ident and native_id are same

- PID
    - OS Module :- getpid()
'''
from threading import Thread
import os


def display() -> None:
    print('Inside display.')
    for i in range(4):
        print("Hello...")


def show() -> None:
    print('Inside show.')
    for i in range(4):
        print("Welcome...")


t1 = Thread(target=display)
t2 = Thread(target=show)

print(f'{t1.ident=}')  # None
print(f'{t1.native_id=}')  # None
# Because it get assigned when thread get started

t1.start()
t2.start()
print(f'{t1.ident=}')
print(f'{t1.native_id=}')
print(f'{os.getpid()=}')
