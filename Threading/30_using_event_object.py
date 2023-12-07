'''
- t1 thread will read 5 file by line from one file
- t2 thread will write these lines into another file
'''
import threading

e = threading.Event()


def read_data() -> None:
    # print("Going to read the file")
    # with open("report.txt") as file1:
    #     data = file1.readlines()
    #     print(f"{data=}")
    pass


def write_data() -> None:
    # print("Going to write data")
    pass


con = threading.Condition()
t1 = threading.Thread(target=read_data)
t2 = threading.Thread(target=write_data)

t1.start()
t2.start()
