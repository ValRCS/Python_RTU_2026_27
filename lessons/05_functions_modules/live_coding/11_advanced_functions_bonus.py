"""Tikai papildus: anotācijas, *args, noklusējuma objekti un rekursija."""

def rectangle_area(width: float, height: float) -> float:
    """Aprēķina taisnstūra laukumu; anotācijas nav runtime validācija."""
    return width * height


def product(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def bad_append(value, values=[]):
    values.append(value)
    return values


def safe_append(value, values=None):
    if values is None:
        values = []
    values.append(value)
    return values


def factorial(number):
    if number < 0:
        raise ValueError("Vajadzīgs nenegatīvs vesels skaitlis.")
    if number <= 1:
        return 1
    return number * factorial(number - 1)


print(rectangle_area(3, 4), rectangle_area.__annotations__)
print(product(2, 3, 4), product())
print("Kopīgs noklusējuma saraksts:", bad_append("a"), end="; ")
print(bad_append("b"))
print("Atsevišķi saraksti:", safe_append("a"), safe_append("b"))
print(factorial(5))
assert factorial(0) == 1
assert factorial(5) == 120
# Rekursiju demonstrēt tikai ar maziem nenegatīviem veseliem skaitļiem.
