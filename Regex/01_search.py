'''
- search()
    - re.search(pattern, data)
    - pattern: the pattern that you want to search
    - data: input string in which you want to search for pattern
    - Return: match object if found otherwise None
    - return first match only
- match()
- finditer()
- findall()
- split()

# flags
- IGNORECASE
'''
import re

pattern = "python"
data = "python is very powerful and python has lots of features"
result = re.search(pattern, data)
print(f"{result=}")
print(f"{type(result)=}")

if result:
    print("Data found ", result.group())
else:
    print("Data not found.")


pattern = "python"
data = "PYTHON is very powerful and it has lots of features"
result = re.search(pattern, data, re.IGNORECASE)
print(f"{result=}")
print(f"{type(result)=}")

if result:
    print("Data found ", result.group())
else:
    print("Data not found.")
