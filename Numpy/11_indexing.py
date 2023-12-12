import numpy as np
print(' 1-D '*10)
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])
print(arr[2])
# print(arr[6])

print(arr[-2])
print(arr[-5])
print(arr[-1])

print(' 2-D '*10)
arr = np.array([[5, 10], [15, 20]])
print(arr.ndim)
print(arr[1])
print(arr[1][0])
print(arr[1][-2])


print(' 3-D '*10)
arr = np.array([[[5, 10, 20], [10, 20, 30]]])
print(arr.ndim)
print(arr[0][1][1])


print(' = '*10)
arr = np.array([10, 20, 30, 40, 50])  # 0 1 2 3 4
for ele in range(arr.size):
    print(arr[ele])
