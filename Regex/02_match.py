'''
- use raw string for pattern becuase excape sequence get ignored in this
- search()
    - re.search(pattern, data)
    - pattern: the pattern that you want to search
    - data: input string in which you want to search for pattern
    - Return: match object if found otherwise None
    - return first match only
- match()
    - search for a pattern at the beginning of a string
    - re.match(pattern, string, flags=0)
    - pattern: the pattern that you want to search
    - data: input string in which you want to search for pattern
    - Return: if match found in start then return object otherwise None
- finditer()
- findall()
- split()

# flags
- IGNORECASE
'''
import re

# pattern = r"python"
# data = "PYTHON is very powerful and it has lots of features"
# # data = "hello, PYTHON is very powerful and it has lots of features"
# result = re.match(pattern, data, re.IGNORECASE)

pattern = re.compile(r"python", re.IGNORECASE)
data = "PYTHON is very powerful and it has lots of features"
result = re.match(pattern, data)

print(f"{result=}")
print(f"{type(result)=}")

if result:
    print("Data found ", result.group())
else:
    print("Data not found.")


'''
- we have two ways of using regular expression
    - directly [pattern (as string)]
    - reguler expression objects using complie method
    - we need to pass flags in the compile method

pattern = re.compile(r"python", re.IGNORECASE)
data = "PYTHON is very powerful and it has lots of features"
result = re.match(pattern, data)

    
'''
