'''
|
- It used for alternation,
- Allowing you to specify multiple patterns and matching any one of them.
'''


import re

# ex-1 get cat or dog
data = "I have a cat and a dog."
pattern = r"cat|dog"

# ex-2 get contact details
data = "admin:- 9090909090\ntest:- test@gmail.com"
pattern = r"\d+|\w+@\w+\.\w+"

result = re.findall(pattern, data)
print(f"{result=}")
