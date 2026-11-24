"""Pārbaude: normāls gadījums, robežgadījums un apzināta kļūme."""
import math


def rectangle_area(width, height):
    return width * height


assert rectangle_area(3, 4) == 12
assert rectangle_area(0, 4) == 0
assert math.isclose(rectangle_area(0.1, 0.2), 0.02)
print("Trīs pārbaudes izturētas.")

# Apzināti nepareiza sagaidāmā vērtība; skripts turpinās.
try:
    assert rectangle_area(3, 4) == 13, "Sagaidījām 13, bet faktiski 12"
except AssertionError as error:
    print("Demonstrācijas kļūme:", error)

# assert nav lietotāja ievades validācija; python -O to var izlaist.
