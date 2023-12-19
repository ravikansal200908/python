# re.M re.MULTILINE
# it mosti used with $ and ^
import re

data = """demo 18
test 30
admin 88"""

pattern = r"\d{2}$"
result = re.findall(pattern, data, re.MULTILINE)
print(f"{result=}")
