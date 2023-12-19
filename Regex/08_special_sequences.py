'''
- Regular expression use special sequences
    - To represent common character classes or groups of character.
'''
import re

text = "Hello, my phone number is 123-456-7890"
# pattern = r'[0-9]'
pattern = r'\d'
# result = re.findall(pattern, text)
# print(f"{result=}")

result = re.finditer(pattern, text)

for data in result:
    print(data.start(), data.end(), data.group())

# \d: Match any digit character
# \D: Match any non-digit character
# \w: Match any word character (alphanumeric plus underscore)
# \W: Match any non-word character
# \s: Match any whitespace character (spaces, tabs, newline, etc.)
# \S: Match any non-whitespace character
# \b: Match a word boundary
# word boundaries are useful for task like searching a specific word in a text
# \A: Startswith
# \Z: Endswith
# .: Match everything
