import numpy as np

# Define two matrices
matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[7, 8], [9, 10], [11, 12]])

# Multiply the matrices using numpy.dot()
result_dot = np.dot(matrix1, matrix2)

# Multiply matrices using the @ operator (available in Python 3.5 and later)
result_at = matrix1 @ matrix2


print("Result using np.dot():")
print(result_dot)

print("\nResult using @ operator:")
print(result_at)

matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
matrix2 = np.array([[1, 2, 3], [4, 5, 6]])

result_elementwise = matrix1 * matrix2
print("\nResult result_elementwise:")
print(result_elementwise)
