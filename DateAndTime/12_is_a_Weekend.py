from datetime import datetime

# date = datetime(2024, 2, 25)  # Example date
date = datetime(2024, 2, 26)  # Example date

print(f'{date.weekday()=}')
if date.weekday() in {5, 6}:
    print("Given date is a weekend.")
else:
    print("Given date is not a weekend.")
