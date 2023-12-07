# We can not return calue in thread
# from threading import Thread


# def display():
#     print('Inside display method.')
#     a = 10
#     b = 30

#     c = a+b
#     print('Total is : ', c)
#     return c


# t1 = Thread(target=display)
# print('t1.start() : ', t1.start())  # None


# In such case we can do one adjustment

from threading import Thread


class MyClass(Thread):
    def __init__(self, val) -> None:
        print('Constructor called')
        # defining value at thread level
        Thread.__init__(self)

    def run(self) -> None:
        a = 10
        b = 20
        self.total = a+b


t1 = MyClass(False)
t1.start()

print('t1.total = ', t1.total)
