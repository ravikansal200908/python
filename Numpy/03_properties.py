'''
ndim, size, shape, dtype, itemsize
min(), max(), sum()
'''
import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

# check dimension
print(f"{arr.ndim=}")

# check number of element in array
print(f"{arr.size=}")

# check total rows and column
print(f"{arr.shape=}")  # return type is tuple

# check datatype
print(f"{arr.dtype=}")

# convert int array to float
arr1 = np.array(arr, dtype=np.float64)
print(f"{arr1=} , {arr1.dtype=}")

# check itemsize of each element, return in bytes
print(f"{arr.itemsize=}")
print(f"{arr1.itemsize=}")

# get total size of array
print(f"array size is : {arr.itemsize * arr.size}")

# finding min, max and sum
print(f"{arr.min()=} , {arr.max()=} , {arr.sum()=}")

print(f"{arr=}")

# find sum according to column, row
print(f"{arr.sum(axis=0)=}")  # column
print(f"{arr.sum(axis=1)=}")  # row
