# We can pass value in init and call another method

from threading import Thread
from time import sleep


videos = ['list', 'tuple', 'set', 'loops']


class MyClass(Thread):
    def __init__(self, val) -> None:
        print('Constructor called')
        # defining value at thread level
        self.kid = val
        Thread.__init__(self)

    def compression(self) -> None:
        print("Vedio compression code")

    def run(self) -> None:
        self.compression()
        if self.kid:
            print("Video compression code")

        for vid in videos:
            print(f"{vid} ---->>>> start uploading")
            sleep(1)
            print(f"{vid} ---->>>> uploaded")


t1 = MyClass(False)
t1.start()

for i in range(4):
    sleep(0.5)
    print('Checking copyrights.')
