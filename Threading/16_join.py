"""
If a thread wants to wait for some other thread,
then we should go for join() method.
"""
from threading import Thread


def display() -> None:
    for i in range(5):
        print("Hello")


def show() -> None:
    for i in range(5):
        print("Welcome")


t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
# t1.join()
t2.start()
t2.join()

for i in range(5):
    print("PYTHON")
