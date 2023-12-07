# Creating threads by extending Thread class
'''
Problem: Suppose we have two functionality:
- Uploading video on youtube.
- Check copyright
'''

from time import sleep
from threading import Thread


videos = ['list', 'tuple', 'set', 'loops']

# def upload(vid) -> None:
#     print(f"{vid} ---->>>> start uploading")
#     sleep(3)
#     print(f"{vid} ---->>>> uploaded")

# for i in videos:
#     upload(i)

# for i in range(4):
#     sleep(0.5)
#     print('Checking copyrights.')


class MyClass(Thread):
    def run(self):
        for vid in videos:
            print(f"{vid} ---->>>> start uploading")
            sleep(1)
            print(f"{vid} ---->>>> uploaded")


t1 = MyClass()
t1.start()

for i in range(4):
    sleep(0.5)
    print('Checking copyrights.')
