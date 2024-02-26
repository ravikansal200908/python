from datetime import datetime, timedelta

date = datetime(2024, 2, 26)  # Example date
days_to_add = 10
new_date = date + timedelta(days=days_to_add)
print("New Date:", new_date)
