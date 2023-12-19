import re

data = "12345$56780 99 4"
# pattern = r'\d'
# pattern = r'\d{2}'
# pattern = r'\d{3}'
pattern = r'\d{2,5}'  # 2 to 5
# pattern = r'\d{2,}'  # mini 2 or max more
# pattern = r'\d{,5}'  # min zero max 5
result = re.findall(pattern, data)

print(f"{result=}")
