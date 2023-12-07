import threading
from time import sleep


def custome_hook(args):
    print("---->>>> Exception occurred in thread.")
    print(f"{args[0]}")  # the exception class
    print(f"{args[1]}")  # exception instance object
    print(f"{args[2]}")  # a traceback object
    print(f"{args[3]}")  # Thread name


def display() -> None:
    sleep(1)
    print("Hello " + 10)


def show() -> None:
    for i in range(5):
        print("Welcome")
        sleep(0.5)


threading.excepthook = custome_hook

t1 = threading.Thread(target=display)
t2 = threading.Thread(target=show)

t1.start()
t2.start()
t1.join()
t2.join()

for i in range(5):
    print("Bye")
