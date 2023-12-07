from threading import Thread, current_thread, Lock

lock = Lock()


class Bus:
    def __init__(self, name, available_setas, lck):
        self.name = name
        self.available_setas = available_setas
        self.lck = lck

    def book_seats(self, need_seats):
        self.lck.acquire()
        print('Available seats are : ', self.available_setas)
        if self.available_setas >= need_seats:
            print(f"{need_seats} are allocated to {current_thread().name}")
            self.available_setas -= need_seats
        else:
            print("Sorry! seats are not available.")
        self.lck.release()


b1 = Bus("Haryana Roadways", 2, lock)
t1 = Thread(target=b1.book_seats, args=(1,), name="Mohit")
t2 = Thread(target=b1.book_seats, args=(1,), name="Mohan")

print(f'{t1.name=}')
print(f'{t2.name=}')

t1.start()
t2.start()
