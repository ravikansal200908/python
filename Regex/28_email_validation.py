'''
- username can contain alphabets (uppercase, lowercase, _, .)
- username can contain digit but can't start with digit
- format should be username@domain.com
- domain must contain alphabets (uppercase, lowercase)
'''

import re

inp = input("Enter email address: ")
pattern = r'^[a-zA-Z_][\w+_\.]+@[a-zA-Z]+\.\w+'
if re.match(pattern, inp):
    print('Email is valid')
else:
    print('Email is invalid')
