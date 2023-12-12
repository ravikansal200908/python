'''
- random()
    - generate random number in [0.0, 1.0]
    - follow uniform distribution
    - numpy.random.random(size=None)
    - numpy.random.random(size=None)
    - size: It's optional, it can be tuple or int.

- rand()
    - generate random number in [0.0, 1.0]
    - follow uniform distribution
    - numpy.random.rand(shape)
    - shape: integer and optional, tuple not allowed

- randn()
    - generate random value as per standard normal distrubution
    - value can be negative

- ranf()
    - same as random function
'''
import numpy as np

print(f"{np.random.random()=}")

arr = np.random.random(3)
print(f"{arr=}")
print(f"{arr.ndim=}")
print(f"{arr.shape=}")


arr = np.random.random((2, 3))
print(f"{arr=}")
print(f"{arr.ndim=}")
print(f"{arr.shape=}")

arr = np.random.rand()
print(f"{arr=}")
arr = np.random.rand(3)
print(f"{arr=}")
arr = np.random.rand(2, 3)
print(f"{arr=}")
print(f"{arr.ndim=}")
print(f"{arr.shape=}")


arr = np.random.randn()
print(f"{arr=}")
arr = np.random.randn(3)
print(f"{arr=}")
arr = np.random.randn(2, 3)
print(f"{arr=}")
print(f"{arr.ndim=}")
print(f"{arr.shape=}")
