'''
- finditer()
    - re.finditer(pattern, string, flags=0)
    - pattern: the pattern that you want to search
    - data: input string in which you want to search for pattern
    - Return: iterator object match info
- findall()
    - It return a list
- split()

# flags
- IGNORECASE
'''
import re

pattern = re.compile('ab', re.IGNORECASE)
data = "abaababa"

result = re.finditer(pattern, data)

print(f"{result=}")
print(f"{type(result)=}")

for out in result:
    print(out)  # return re.match data
    print(out.start())  # return start index
    print(out.end())  # return end index
    print(out.group())  # it return matched data

"""
total occurance: 3
first: 0
second: 3
third: 5
"""

pattern = re.compile('ab', re.IGNORECASE)
data = "abaababa"

result = re.findall(pattern, data)

print(f"{result=}")
print(f"{type(result)=}")

'''
- finditer is memory efficient, beacuse findall return list
- findall only return result while finditer return more information
'''
