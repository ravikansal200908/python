'''
- t1 thread will switch the light.
- t2 thread will blink the message.
'''


import threading
import time

e = threading.Event()


def light_switch() -> None:
    while True:
        print('Light is green.')
        e.set()  # Set flag to True So that t2 can execute
        time.sleep(5)
        print("Light is red.")
        e.clear()  # Set flag to false t2 will stop execution
        time.sleep(5)
        e.set()  # Set flag to True So that t2 can execute


def traffic_message() -> None:
    e.wait()  # t2 wait initialy
    while e.is_set():
        print("You Can Go!!!!!")
        time.sleep(0.5)
        e.wait()  # so that t2 thread can wait after it's execution


t1 = threading.Thread(target=light_switch)
t2 = threading.Thread(target=traffic_message)

t1.start()
t2.start()
