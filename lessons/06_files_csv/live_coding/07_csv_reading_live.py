import csv
from io import StringIO

with open("datasets/expenses.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    print("Galvene:", next(reader))
    print("Saraksts:", next(reader))
with open("datasets/expenses.csv", encoding="utf-8", newline="") as file:
    row = next(csv.DictReader(file))
    print("Vārdnīca:", row, type(row["amount_eur"]))
    print(float(row["amount_eur"]))
line = 'food,"maize, rupjā",2.15'
print("split:", line.split(","))
print("csv:", next(csv.reader(StringIO(line))))
