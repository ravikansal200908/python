import calendar
from datetime import datetime

year = 2024
month = 2

first_day = datetime(year, month, 1)
last_day = datetime(year, month, calendar.monthrange(year, month)[1])

print("First day : ", calendar.day_name[first_day.weekday()])
print("Last day:", calendar.day_name[last_day.weekday()])
