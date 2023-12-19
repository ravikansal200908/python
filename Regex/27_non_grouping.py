'''
- (?:...) # ?
- If we have to skip one character then ? is fine.
- But for multiple character case we can use non-grouping
'''

import re

data = "Visit http://www.example.com or http://example.com"
# pattern = r'https?://www\.\w+\.\w+'
pattern = r'https?://(?:www\.)?\w+\.\w+'
result = re.findall(pattern, data)

print(f'{result=}')
