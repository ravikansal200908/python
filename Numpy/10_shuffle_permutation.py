'''
shuffle change in array while permutation generate new array
'''
import numpy as np

arr = np.array([1, 4, 7, 9])

print(f"{arr=}")
np.random.shuffle(arr)
print(f"{arr=}")


print(f"{arr=}")
np.random.permutation(arr)
print(f"{arr=}")
