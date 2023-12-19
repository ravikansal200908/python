import re

pattern = r"bb"
data = "bbbababa"  # match at 0 or at 1

print(re.findall(pattern, data))  # show one output only

# if second match get overlapped with first match
# then it will not consider this sitiuations.
