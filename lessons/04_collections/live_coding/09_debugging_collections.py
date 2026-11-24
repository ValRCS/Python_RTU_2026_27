"""Kļūdu demonstrācijas: katra kļūda izolēta, skripts turpina darbu."""
# Prognozē kļūdas tipu, tad palaid bloku. try/except no 3. nodarbības.
try:
    print([1, 2][2])
except IndexError as error:
    print("IndexError:", error)

try:
    print({"x": 1}["y"])
except KeyError as error:
    print("KeyError:", error)

try:
    [1, 2].remove(3)
except ValueError as error:
    print("ValueError:", error)

try:
    point = (1, 2)
    point[0] = 3
except TypeError as error:
    print("TypeError:", error)

try:
    print(", ".join([1, 2]))
except TypeError as error:
    print("TypeError:", error)

try:
    numbers = []
    print(sum(numbers) / len(numbers))
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)

try:
    items = [1]
    items = items.append(2)
    items.append(3)
except AttributeError as error:
    print("AttributeError:", error)

# Loģiskas kļūdas: programma darbojas, bet rezultāts nav pareizs.
data = {"vārds": "Anna"}
print("Anna" in data, "Anna" in data.values())
a = [1, 2]
b = a
b.append(3)
print("Kopīgs objekts:", a, b)
c = a.copy()
c.append(4)
print("Neatkarīga kopija:", a, c)

# Kļūdaina dzēšana iterācijas laikā var izlaist elementus.
numbers = [2, 4, 6, 7]
for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
print("Kļūdains rezultāts:", numbers)  # [4, 7]
remaining = []
for number in [2, 4, 6, 7]:
    if number % 2 != 0:
        remaining.append(number)
print("Pareizs rezultāts:", remaining)  # [7]
