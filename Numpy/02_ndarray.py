import numpy as np

arr = np.array([10, 20, 30, 40])
print(f"{arr=} , {type(arr)=}")

# total_num = int(input("Enter total number of element in array : "))
# data = []
# for _ in range(total_num):
#     inp = int(input("Enter a number : "))
#     data.append(inp)

# arr = np.array(data)
# print(f"{arr=}")
# print(f"{arr.ndim=}")


# create zero dim array
arr = np.array(10)
print(f"{arr=}")
print(f"{arr.ndim=}")

# create 2D array
arr = np.array([[10, 20, 30]])
print(f"{arr=}")
print(f"{arr.ndim=}")

# create 3D array
arr = np.array([[10, 20, 30]])
print(f"{arr=}")
print(f"{arr.ndim=}")


# create 10D array
arr = np.array([10, 20, 30], ndmin=10)
print(f"{arr=}")
print(f"{arr.ndim=}")
