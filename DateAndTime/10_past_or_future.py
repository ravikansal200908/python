from datetime import datetime

date = datetime(2024, 2, 25)  # Example date
if date < datetime.now():
    print("Date is in the past.")
else:
    print("Date is in the future.")

date = datetime(2024, 3, 25)  # Example date
if date < datetime.now():
    print("Date is in the past.")
else:
    print("Date is in the future.")
