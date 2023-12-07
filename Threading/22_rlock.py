'''
Need for RLock
'''
from threading import RLock, Thread

mylock = RLock()


def get_first_line():
    mylock.acquire()
    print('Fetching first line')
    mylock.release()


def get_second_line():
    mylock.acquire()
    print('Fetching second line')
    mylock.release()


def main():
    mylock.acquire()
    get_first_line()
    get_second_line()
    mylock.release()


t1 = Thread(target=main)
t1.start()
