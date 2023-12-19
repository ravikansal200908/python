import re

pattern = re.compile('dog|cat', re.IGNORECASE)
data = "I saw a dog running behind cat and cat climbed but dog couldn't"

match_iter = re.finditer(pattern, data)
count = 0

for i in match_iter:
    count += 1
    print(i)

print(f"{count=}")
