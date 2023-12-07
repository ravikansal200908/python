from threading import Thread


def display(n, msg):
    for i in range(n):
        print(msg)


# t1 = Thread(target=display, args=(10, "asdfghjkl"))
t1 = Thread(target=display, kwargs={'n': 10, 'msg':"asdfghjkl"})
t1.start()


for i in range(5):
    print("Learn Python")
