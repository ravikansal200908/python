from datetime import datetime


def calculate_age(birth_date):
    today = datetime.now()
    return (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )


birth_date = datetime(1994, 8, 15)  # Example birth date
age = calculate_age(birth_date)
print("Age:", age)
