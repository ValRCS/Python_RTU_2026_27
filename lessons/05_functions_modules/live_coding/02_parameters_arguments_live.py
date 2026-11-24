"""Pozicionālie, atslēgvārdu un noklusējuma argumenti."""

def area(width, height):
    return width * height


def power(base, exponent=2):
    return base ** exponent


print(area(3, 5))
print(area(height=5, width=3))
print(power(4), power(4, 3), power(base=2, exponent=5))
# Kāpēc power(4) darbojas, bet area(4) ne?
try:
    area(4)
except TypeError as error:
    print(type(error).__name__, error)

# Papildus: bool parametrs, ko ērti nodot ar atslēgvārdu.
def format_price(amount, currency="EUR"):
    return f"{amount:.2f} {currency}"


print(format_price(3.9))
print(format_price(3.9, currency="USD"))
