# Create thread and adding kwargs
# import Thread class
from threading import Thread


# Create a function containing code to be executed parallaly
def display(n, msg):
    for i in range(n):
        print(msg)


# Create new thread
t1 = Thread(target=display, kwargs={'n': 5, 'msg': "Hi Pyhon"})

# Start the new thread
t1.start()


for i in range(4):
    print("Welcome")

'''
Here we have 2 thread t1 and main,
If we run the code again and again then
we can see some difference in the output.
'''
