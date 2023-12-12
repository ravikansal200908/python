# create a matrix
import numpy as np

# square matrix
mat = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"{mat}")
print(f"{mat.shape=}")


# transpose of a matrix
trans = mat.T
print(f"{trans}")

# identity matrix
arr = np.eye(3, dtype='int')
arr = np.eye(3, 4, dtype='int')
print(arr)


# creating a matrix having any number in diagonal
arr = np.diag([11, 22, 33, 44])
print(arr)

# getting a diagonal element
print(np.diag(arr))
