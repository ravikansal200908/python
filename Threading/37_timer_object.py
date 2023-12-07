import threading
from time import sleep


def task(msg: str) -> None:
    for i in range(5):
        print(msg)
        sleep(0.3)


# Task method will me executed after 10 seconds
timer = threading.Timer(5, task, ("Hi Python",))
timer.start()

for i in range(5):
    print("Main thread")
