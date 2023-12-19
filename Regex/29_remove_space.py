import re

text = '   this   is   a   sentence   with   spaces.   '
text = text.strip()

pattern = r'\s+'
result = re.sub(pattern, ' ', text)
print(f'{result=}')
