'''
Need of condition object:
    - to communicate with multiple threads.
    - Producer and consumer problem is an example of it

Used method:
- acquire() : Used to acquire the lock
- release() : Used to release the lock
- wait(timeout=0) : Used to block the thread
- notify() : Wake up one thread
- notify_all() : Wake up multiple thread
- 9,10,11 must be called when the calling thread has acquire the lock
'''
import threading


def write_data() -> None:
    con.acquire()
    with open("report.txt", "w") as file1:
        days = [
            "Monday",
            "Tuesday",
            "Wesnesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        for day in days:
            temp = input(f"Enter the temprature for {day} : ")
            file1.write(temp+"\n")
    con.notify_all()
    con.release()


def max_temp() -> None:
    con.acquire()
    con.wait(timeout=0)
    with open("report.txt") as file1:
        data = file1.readlines()
        max1 = float(data[0].strip("\n"))
        for temp in data[1:]:
            temp = float(temp.strip("\n"))
            if temp > max1:
                max1 = temp
        print("Max temprature is : ", max1)
        con.release()


def avg_temp() -> None:
    con.acquire()
    con.wait(timeout=0)
    with open("report.txt") as file1:
        data = file1.readlines()
        sum1 = 0
        for temp in data[1:]:
            temp = float(temp.strip("\n"))
            sum1 += temp
        avg = sum1 / len(data)
        print("Avg temprature is : ", sum1)
        print("Avg temprature is : ", avg)
        con.release()


con = threading.Condition()
t1 = threading.Thread(target=write_data)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)

t1.start()
t2.start()
t3.start()
