# Need of join method.
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
t2.start()

# Main thread code
for i in range(4):
    print("Hello....")


# If you run the above code it will send the notification before uploading
# In such case we need join method.
