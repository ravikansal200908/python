# re.I re.IGNORECASE

import re

data = "I love python programming. PyTHon is awesome!"

# pattern = r"\bpython\b"
# result = re.findall(pattern, data)

# pattern = r"\bpython\b"
# result = re.findall(pattern, data, re.IGNORECASE)

pattern = re.compile(r"\bpython\b", re.IGNORECASE)
result = re.findall(pattern, data)

print(f"{result=}")
