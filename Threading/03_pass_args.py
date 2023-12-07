# Create thread and adding args
# import Thread class
from threading import Thread


# Create a function containing code to be executed parallaly
def display(n, msg):
    for i in range(n):
        print(msg)


# Create new thread
t1 = Thread(target=display, args=(5, "Hi Pyhon"))

# Start the new thread
t1.start()
