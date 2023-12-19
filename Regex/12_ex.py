import re

data = "My email addresses are test@gmail.com and test12@gmail.com"
pattern = r"\w+@\w+\.\w+"

result = re.findall(pattern, data)
print(f"{result=}")

# *: 0 or more
# +: 1 or more

# Expected output
# a should occur 0 or more time and b can be 1 or more
# ['abb', 'aaabbb', 'aaabbcc', 'bb']
data = "abb ac aaabbb aaa aaabbcc cc bb"
# pattern = r"a*b+\w+"
pattern = r"a*b+[a-z]+"
result = re.findall(pattern, data)
print(f"{result=}")
