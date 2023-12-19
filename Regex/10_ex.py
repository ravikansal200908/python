# find date from text
import re

text = """
Today is 2023-10-02, and I have a meeting scheduled for 2023-10-05
"""
pattern = r"\d{4}-\d{2}-\d{2}"
result = re.finditer(pattern, text)

for data in result:
    print('--->', data.group())
