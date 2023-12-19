'''
?
- it specifies that the preceding character of grop is optional
'''


import re

# ex-1 fetch colour or color
data = "colour and color are same"
pattern = r"colou?r"


# ex-2 fetch mobile number
data = "Call me at 123-456-7890 or 1234567890"
pattern = r"\d{3}-?\d{3}-?\d{4}"

result = re.findall(pattern, data)
print(f"{result=}")


# ex-2 validate all URL
urls = ['http://Exam.com', 'https://example123.com', 'htttp://fileserver.com']
pattern = r"\d{3}-?\d{3}-?\d{4}"

for url in urls:
    if result := re.findall(pattern, url):
        print('Valid URL: ', result)
    else:
        print('Inalid URL: ', url)
