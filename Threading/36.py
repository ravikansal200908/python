# daemon thread examples

from threading import Thread
from time import sleep


# # Example-1
# def display() -> None:
#     for i in range(5):
#         print("Teaching session ", i)
#         sleep(0.7)


# t1 = Thread(target=display)
# t1.daemon = True  # comment this line and check output
# t1.start()

# sleep(3)
# print("Exam time!!")
# print("Exam over.")


# Example-2
def syntax_highlighting() -> None:
    for i in range(10):
        print("Syntax highlighting ")
        sleep(0.7)


t1 = Thread(target=syntax_highlighting)
t1.daemon = True  # comment this line and check output
t1.start()

sleep(3)
print("Close the application.!!")
