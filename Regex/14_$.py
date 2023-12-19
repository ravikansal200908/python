'''
$
- It ensure that patten only matches when it appears at end of the input
'''

import re

data = """the code is 123
and final code is 999"""
# pattern = r"\d$"  # check if ending with digit
pattern = r"\d{3}$"  # check if ending with 3 digit

result = re.findall(pattern, data)
# result = re.findall(pattern, data, re.MULTILINE)
print(f"{result=}")
