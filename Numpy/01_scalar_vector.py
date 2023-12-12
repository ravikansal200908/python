'''
A numpy array is a collection of values which are of same type.
These vaues contain below information:
- raw data
- how to locate element
- how to interpret an element

- In array we need not to seprate element by comma.
- A value with no dimention is called scalar ex. 30
- One dimentional is calle vector 3x [10 20 30]
- 2D is called matrix
- 3D is called tensor

'''

import numpy as np

arr = np.array([10, 20, 30])

print(f'{arr=}, {type(arr)}')
