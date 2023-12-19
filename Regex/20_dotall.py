# re.S re.DOTALL
import re

data = "hello\nworld"
pattern = r"."
result = re.findall(pattern, data, re.DOTALL)

print(f"{result=}")
