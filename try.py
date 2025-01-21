def div(a, b):
    if b == 0:
        raise ArithmeticError()
    return a / b

try:
    div(10, 0)
except ZeroDivisionError as ex:
    print("Rechenfehler: " + ex)
except ArithmeticError as ex:
    print("Divisionfehler")
except Exception as ex:
    print("Ausnahmefehler")


def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    return "Valid age!"

try:
    print(check_age(16))
except ValueError as e:
    print(e)