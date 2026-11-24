"""print, return, agrīna atgriešana un kortežu izpakošana."""

def double_print(number):
    print(number * 2)


def double_return(number):
    return number * 2


def classify(number):
    if number < 0:
        return "negatīvs"
    if number == 0:
        return "nulle"
    return "pozitīvs"


def get_statistics(numbers):
    """Tukšam sarakstam atgriež None; citādi (min, max, sum)."""
    if not numbers:
        return None
    return min(numbers), max(numbers), sum(numbers)


a = double_print(5)
b = double_return(5)
print(a, b, b + 3)
for value in [-2, 0, 5]:
    print(value, classify(value))

result = get_statistics([12, 15, 8, 17, 11])
print(result, type(result))
lowest, highest, total = result
print(lowest, highest, total)
print(get_statistics([]))
# Tukšu rezultātu nepakojam trīs mainīgajos.
assert result == (8, 17, 63)
