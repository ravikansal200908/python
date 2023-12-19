'''
^
- It ensure that patten only matches when it appears at beginning of the input
- Negation of character classes
'''

import re

# # Use 1
# data = "hello world"
# pattern = r"^hello"

# data = "hello world"
# pattern = r"^world"

# data = "4hello world"
# pattern = r"^\d"


# Use 2
data = "hello 10 56world"
pattern = r"[0-9]"

data = "hello 10 56world"
pattern = r"[^0-9]"

result = re.findall(pattern, data)
print(f"{result=}")
