'''
- condition for password:
    - contain at lease one digit or at least one uppercase letter
'''
import re

password = input("Enter password: ")
pattern = '[0-9A-Z]'

if re.findall(pattern, password):
    print("Valid password.")
else:
    print("Invalid password.")
