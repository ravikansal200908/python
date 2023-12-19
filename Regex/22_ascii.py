# re.A re.ASCII

import re

data = "Hello 12 World, non-ASCII character like é, à and ö should be ignored."
pattern = r"\b\w+\b"
result = re.findall(pattern, data, re.ASCII)

print(f"{result=}")
