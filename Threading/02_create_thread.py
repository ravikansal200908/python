'''
Two ways of creating a thread
- Using Thread class preset in threading module.
- Extending, Thread class
'''

# import Thread class
from threading import Thread


# Create a function containing code to be executed parallaly
def display():
    for i in range(4):
        print("Hello Python")


# Create new thread
t1 = Thread(target=display)

# Start the new thread
t1.start()
