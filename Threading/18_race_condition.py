'''
- Race Condition :
    It's a bug generated when you do multi-procession.
    It occurs because two or more threads tries to update the
    same variable and result into unriable output.
'''

from threading import Thread, current_thread


class Bus:
    def __init__(self, name, available_setas):
        self.available_setas = available_setas

    def book_seats(self, need_seats):
        print('Available seats are : ', self.available_setas)
        if self.available_setas >= need_seats:
            print(f"{need_seats} are allocated to {current_thread().name}")
            self.available_setas -= need_seats
        else:
            print("Sorry! seats are not available.")


b1 = Bus("Haryana Roadways", 2)
t1 = Thread(target=b1.book_seats, args=(1,), name="Mohit")
t2 = Thread(target=b1.book_seats, args=(1,), name="Mohan")

print(f'{t1.name=}')
print(f'{t2.name=}')

t1.start()
t2.start()

'''
Thread synchorization technique:
    - It ansure that two or more concurrent threads do not simultaneously
    execute some particular program segment knowm as critical section.
    - A common approach is to protect the cretical section
    of code. (Prevent concurrent access.)
    Techniques:
        - Using Locks
        - Using R-Lock
        - Using Semaphores
'''
