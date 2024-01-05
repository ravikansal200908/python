# grouping metacharacter (...)
import re

data = "Email address: admin1@gmail.com, test@example.com, user1@yahoo.com"
# pattern = r'\w+@\w+\.\w+'
pattern = r'(\w+)(@\w+\.)(\w+)'
result = re.findall(pattern, data)

# problem fetch username and domain via group not @
# pattern = r'(\w+)@(\w+\.\w+)'
pattern = r'(\w+)@(\w+)\.(\w+)'
result = re.findall(pattern, data)

print(f'{result=}')
