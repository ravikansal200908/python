# Configure thread names

from threading import Thread, current_thread


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
print(f'{t1.getName()=}')
print(f'{t2.name=}')

# change thread name
# t1.name = "Changed_name"
t1.setName("Changed_name")
print(f'{t1.name=}')

# change current thread name
print(f'{current_thread().name=}')
current_thread().name = "Current_thread_new_name"
print(f'{current_thread().name=}')
