'''
- Queue works on FIFO
- put(item, block=True)
    - Used to insert element into queue
    - block false will raise exception if queue limit reachs
- get()
    - Used to delete element from queue
    - Remove data from start
'''

import threading
from queue import Queue


def producer(my_que) -> None:
    print('producer: running')

    n = int(input('Enter number of students : '))
    for i in range(n):
        marks = float(input('Enter Marks : '))
        my_que.put(marks)
    my_que.put(None)  # it shows end of queue
    print('producer: end')


def consumer(my_que) -> None:
    print('consumer: running')
    while True:
        item = my_que.get()
        if item is None:
            break
        print(f'Got {item}')
    print('consumer: end')


my_que = Queue()

t1 = threading.Thread(target=producer, args=(my_que,))
t2 = threading.Thread(target=consumer, args=(my_que,))
t1.start()
t2.start()

'''
By default it handle thread communication and locking
'''
