

# calculate_age.py

from datetime import datetime

def calculate_age_in_days(birthdate_str, today=None):
    try:
        birthdate_obj = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        if today is None:
            today = datetime.now().date()
        print("Birthdate:", birthdate_obj)  # Dodaj ispis datuma rođenja
        print("Today:", today)  # Dodaj ispis trenutnog datuma
        age_in_days = (today - birthdate_obj).days
        if age_in_days < 0:
            return "Birthdate cannot be in the future."
        return str(abs(age_in_days))  # Dodaj apsolutnu vrednost radi obezbeđivanja pozitivnog broja dana
    except ValueError:
        return "Invalid date format. Please enter the date in the format YYYY-MM-DD."
