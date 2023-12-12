'''
- zeros()
    - create a n-d-array and fill all value with 0's.
    - np.zeros(shape, dtype=float, order='C')
    - shape either integer(1D) or tuple(ND)
    - default value of dtype is float, order is row and column major
- ones()
    - create a n-d-array and fill all value with 0's.
    - np.ones(shape, dtype=float, order='C')
    - shape either integer(1D) or tuple(ND)
    - default value of dtype is float, order is row and column major
- arange()
    - behaves exactly same as range() function
- linspace()
    - returns array containing linearly spaced values
'''

import numpy as np

arr = np.zeros(4)
print(f"{arr=}")
print(f"{arr.ndim=}")
print(f"{arr.shape=}")
print(f"{arr.dtype=}")
print("-"*20)

# arr = np.ones(4, dtype='int')
# arr = np.ones((2, 3), dtype='int')
# arr = np.ones((2, 3), dtype='tuple')  # it will show error
arr = np.ones((2, 3), dtype=[('x', 'int'), ('y', 'float')])
arr = np.ones((2, 3), dtype='int')*4
print(f"{arr=}")
print(f"{arr.ndim=}")
print(f"{arr.shape=}")
print(f"{arr.dtype=}")

# arange
print(f"{np.arange(2, 10, 1)=}")
print(f"{np.arange(2, 10, 2, dtype='float')=}")

# linspace
print(f"{np.linspace(1, 10, 7)=}")
print(f"{np.linspace(1, 10, 7, dtype='int')=}")
