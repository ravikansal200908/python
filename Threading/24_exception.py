from threading import Thread
from time import sleep


def display() -> None:
    sleep(1)
    print("Hello " + 10)


def show() -> None:
    for i in range(5):
        print("Welcome")
        sleep(0.5)


t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
t2.start()
t1.join()
t2.join()

for i in range(5):
    print("Bye")


'''
- here we have an exception in the display
- What happens for exception in thread?
    - the interpreter calls threading.excepthook()
    with one argument i.e. named tuple with 4 arguments
        - the exception class
        - exception instance object
        - a traceback object
        - Thread name

For main thread -----> sys.excepthook
For created thread --> threading.excepthook --> sys.excepthook
'''
