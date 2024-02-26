import calendar

year = 2024
month = 2
num_days = calendar.monthrange(year, month)
print(f'{num_days=}')
print("Number of days in the month:", num_days[1])
