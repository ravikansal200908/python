# \d: Match any digit character
# \D: Match any non-digit character
# \w: Match any word character (alphanumeric plus underscore)
# \W: Match any non-word character
# \s: Match any whitespace character (spaces, tabs, newline, etc.)
# \S: Match any non-whitespace character
# \b: Match a word boundary
# word boundaries are useful for task like searching a specific word in a text
# \A: Startswith
# \Z: Endswith
# .: Match everything

import re

text = "Hello, my_phone $%^ number . is 1234"
# pattern = r'\d'
# pattern = r'\D'
# pattern = r'\w'
# pattern = r'\W'
# pattern = r'\s'
# pattern = r'\S'
# pattern = r'\bmy_phone\b'
# pattern = r'\AHello'
# pattern = r'1234\Z'
# pattern = r'.'  # If i have to find . only then things would be different
# pattern = r'e'
pattern = r'\.'

result = re.finditer(pattern, text)

for out in result:
    print(out.start(), '--->>', out.group(), end=" ")
