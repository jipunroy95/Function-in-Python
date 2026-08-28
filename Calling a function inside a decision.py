def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

age = 20
print(check_age(age))