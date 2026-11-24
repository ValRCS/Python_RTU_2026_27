"""Standarta bibliotēkas moduļi; nekas nav jāinstalē."""
import math
import random
from statistics import mean, median
import datetime as dt


print(math.sqrt(81), math.ceil(3.2), math.pi)
numbers = [3, 4, 8, 20]
print(mean(numbers), median(numbers))
# Lokāls ģenerators ar sēklu atkārtojamai demonstrācijai.
rng = random.Random(42)
print("Kauliņš:", rng.randint(1, 6))
print("Izvēle:", rng.choice(["Rīga", "Cēsis", "Liepāja"]))
lesson = dt.date(2026, 11, 26)
print("Pēc nedēļas:", lesson + dt.timedelta(days=7))
# Papildus: date.today() ir atkarīgs no datora datuma.
# Nepārsauc savu failu par random.py, math.py vai statistics.py.
