from datetime import datetime

date_str = "2023-12-25"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print("Datetime Object : ", date_obj)
