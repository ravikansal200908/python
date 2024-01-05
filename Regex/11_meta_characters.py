'''
- Metacharacters
    - It affect how the regular expressions around them are interpreted
    - It don't match themselves, Insted, they indicate some rules.
    - . (Dot)
    - ^ (Caret)
    - $ (Dollar)
    - * (asterisk)
    - + (Plus)
    - ? (Question mark)
    - [] (Square brackets)
    - | (Pipe)
    - \
    - (...)
    - [^...]
'''

import re

# data = "Hello\\nworld, i am ravi kansal."
data = "Hello world, i am ravi kansal."
# pattern = r"."
# pattern = r"l"
# pattern = r"l+"  # either 1 or more than 1
# pattern = r"he+"  # h will occure 1 time and e can occur 1 or more time
pattern = r"h+e+"  # he both can occur 1 or more time


data = "marks are 90,45,67,333,21"
pattern = r"\d\d"
pattern = r"\d{2}"
pattern = r"\d+"  # \d should occure 1 or more time


result = re.finditer(pattern, data)
for out in result:
    print(out)
