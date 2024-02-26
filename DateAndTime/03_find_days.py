from datetime import datetime


def days_between_dates(date1, date2):
    delta = date2 - date1
    return delta.days


date1 = datetime(2023, 8, 9)  # Example start date
date2 = datetime(2023, 8, 20)  # Example end date
num_days = days_between_dates(date1, date2)
print("Number of days between the dates:", num_days)
