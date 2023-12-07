'''
- Using RLock, you can acquire() multile times.
- RLock is just modified version of the Lock.
- It contain information for current thread as well
'''
from threading import Thread, current_thread, RLock

lock = RLock()


class Bus:
    def __init__(self, name, available_setas, r_lck):
        self.name = name
        self.available_setas = available_setas
        self.r_lck = r_lck

    def book_seats(self, need_seats):
        print('==============>>>> ', self.r_lck)
        self.r_lck.acquire()
        self.r_lck.acquire()
        print('Available seats are : ', self.available_setas)
        if self.available_setas >= need_seats:
            print(f"{need_seats} are allocated to {current_thread().name}")
            self.available_setas -= need_seats
        else:
            print("Sorry! seats are not available.")
        self.r_lck.release()
        self.r_lck.release()


b1 = Bus("Haryana Roadways", 2, lock)
t1 = Thread(target=b1.book_seats, args=(1,), name="Mohit")
t2 = Thread(target=b1.book_seats, args=(1,), name="Mohan")

print(f'{t1.name=}')
print(f'{t2.name=}')

t1.start()
t2.start()
