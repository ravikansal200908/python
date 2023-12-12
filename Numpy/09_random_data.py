import numpy as np

# will print random number from below sequence
# every value has same probability
print(f"{np.random.choice([10, 6, 7, 8])=}")

# set size
print(f"{np.random.choice([10, 6, 7, 8], size=(2, 3))=}")


# set probability
# it's sum must be one othewise it shows error
arr = np.random.choice(
    [10, 6, 7, 8],
    size=(2, 3),
    p=[0.1, 0.3, 0.6, 0.0]
    )
print(f"{arr=}")

arr = np.random.choice(
    [10, 6, 7, 8],
    size=(2, 3),
    p=[1.0, 0.0, 0.0, 0.0]
    )
print(f"{arr=}")
