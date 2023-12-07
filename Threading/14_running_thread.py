'''
- Count of current running thread
- Details of all threads
- Built in functions
    - is_alive() :- Check thread is running or not
    - main_thread() :- Returns main threads details
    - active_count() :- Number of running threads
    - enumerate() :- List of all running threads
    - get_native_id() :- Know native id of thread
'''

from threading import (
    Thread,
    main_thread,
    active_count,
    enumerate,
    get_native_id
)


def display() -> None:
    # display main thread information
    print(f'{main_thread()=}')
    print("Native id of t1 thread : ", get_native_id())
    for i in range(4):
        print("Hello")


def show() -> None:
    for i in range(4):
        print("Welcome")


t1 = Thread(target=display)
print("Before : ", t1.is_alive())
t1.start()
print("Number of running threads : ", active_count())
print("List of all running threads : ", enumerate())
print("Native id of main thread : ", get_native_id())
print("After : ", t1.is_alive())
