import re

# Problem-1 group link and label
data = '<a href="https://www.example.com">Click here</a>'
# pattern = r'<a href="[^"]+">[^<]+</a>'
pattern = r'<a href="([^"]+)">([^<]+)</a>'
result = re.findall(pattern, data)

# Problem-2 extract month/year and date
data = 'incidents hapened on 10/13/2023 12:33:40 and 11/10/2022 01:45:31'
# pattern = r'\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}'
pattern = r'\d{2}/(\d{2}/\d{4})\s\d{2}:\d{2}:\d{2}'
result = re.findall(pattern, data)

print(f"{result=}")
