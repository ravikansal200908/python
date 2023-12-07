# Create thread for class method
from threading import Thread


class Example:
    @classmethod
    def display(cls, n) -> None:
        for i in range(n):
            print("Hi User")


t1 = Thread(target=Example.display, args=(5,))
t1.start()

for i in range(5):
    print("Welcome")
