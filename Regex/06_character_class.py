'''
- character class
    - set of character that you can define using regular expression

'''
import re

# pattern = r'[0-9]'  # character class
# pattern = r'[a-z]'  # a-z
# pattern = r'[A-Z]'  # A-Z
# pattern = r'[a-zA-Z]'  # a-z and A-Z
# pattern = r'[a-z0-9]'  # a-z and 0-9
pattern = r'[^a-z0-9]'  # exclude a-z and 0-9
# pattern = r'[aeiou]'  # match specific character
# pattern = r'[$#]'  # match specific character
# pattern = r'\d'  # meta class
data = 'The price is $100'

# match_list = re.findall(pattern, data, re.IGNORECASE)
match_list = re.findall(pattern, data)
print(f"{match_list=}")

'''
- [abc]: Matches any one of the character a,b,c
- [^abc]: Matches any one of the character that is not a,b,c
- [0-9]: Matches any digit from 0-9
- [A-Z]: Matches any uppercase letter from A-Z
- [a-z]: Matches any lowercase letter from a-z
- [A-Za-z]: Matches any uppercase and lowercase a-z and A-Z
- [0-9A-Fa-f]: Matches any hexdecimal digit
- [a-zA-Z0-9]: Matches any alphanumeric character
- [^0-9]: Matches any character that is not digit
- [^a-zA-Z]: Matches any character that is not uppercase or lower case
'''
