# re.X re.VERBOSE
# Used to ignore comment at the time of pattern

import re

data = "Hello.World"
# pattern = r"\w+\.\w+#matched data"
# pattern = r"\w+#matched data.\w+"
# pattern = r"\w+(?#matched data)\.\w+"
pattern = r"""\w+ #for alphanumeric
\. #for matching dot
\w+ #for matching alphanumeric"""
result = re.findall(pattern, data, re.VERBOSE)

print(f"{result=}")
