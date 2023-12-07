'''
We can not directly create __init__ method in MyClass
Because Threa class init needs to be execute to create threads
'''
from threading import Thread
from time import sleep


videos = ['list', 'tuple', 'set', 'loops']


class MyClass(Thread):
    # def __init__(self):
    #     print('Constructor called.')

    def __init__(self):
        print('Constructor called.')
        Thread.__init__(self)

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
