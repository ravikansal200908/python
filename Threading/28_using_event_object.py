import threading
import time

e = threading.Event()


def task() -> None:
    print("Game is started.")
    time.sleep(5)
    e.set()


def end() -> None:
    e.wait()
    if e.is_set():
        print("Code to destroying session.")


t1 = threading.Thread(target=task)
t2 = threading.Thread(target=end)
t1.start()
t2.start()
