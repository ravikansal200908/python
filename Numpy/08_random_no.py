'''
- randint()
    - One of function for doing random sampling
    - Syntax: np.random.randint(low, high=None, size=NOne, dtype='int')

- random_integers()
    - It same as above but it's a old function.
    - It's removed.

- seed()
    - if we want same random no again for the calculation purpose, then use it
    - it's range is 2**32
'''
import numpy as np

# if we pass one value then it considered as high
arr = np.random.randint(10)  # [low, high)
print(f"{arr=}")

arr = np.random.randint(10, 20)  # [low, high)
print(f"{arr=}")

arr = np.random.randint(10, 20, (2, 3), dtype='int64')
print(f"{arr=}")


np.random.seed(100)
arr = np.random.randint(10, 20, (2, 3))
print(f"{arr=}")
