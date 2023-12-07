from threading import Thread
from time import sleep


def upload():
    print("Uploadin start.")
    sleep(3)
    print("Video uploaded.")


def notification():
    print("Sending notification to users.")


t1 = Thread(target=upload)
t2 = Thread(target=notification)

t1.start()
t1.join()
t2.start()
t2.join()

# Main thread code
for i in range(4):
    print("Hello....")
