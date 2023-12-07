# Create thread for class method
from threading import Thread


class Example:
    def display(self) -> None:
        for i in range(5):
            print("Hi User")


e1 = Example()
t1 = Thread(target=e1.display)
t1.start()

for i in range(5):
    print("Welcome")
