# how to change daemon nature of thread?

from threading import Thread


def display() -> None:
    print("This is display function")

    # create new thread and check it daemon nature
    t2 = Thread(target=demo)
    print("Daemon nature of t2 is : ", t2.daemon)


def demo() -> None:
    print("This is demo function")


t1 = Thread(target=display)
print("Daemon nature of t1 is : ", t1.daemon)
# t1.setDaemon(True)
t1.daemon = True
print("Daemon nature of t1 is : ", t1.daemon)
t1.start()
# t1.daemon = False
# print("Daemon nature of t1 is : ", t1.daemon)
