# print thread information
# import Thread class
from threading import Thread, current_thread


# Create a function containing code to be executed parallaly
def display(n, msg):
    print('t1 thread details: ', current_thread())
    print('t1 thread details: ', current_thread().name)
    for i in range(n):
        print(msg)


# Create new thread
t1 = Thread(target=display, kwargs={'n': 5, 'msg': "Hi Pyhon"})

# Start the new thread
t1.start()


for i in range(4):
    print("Welcome")
