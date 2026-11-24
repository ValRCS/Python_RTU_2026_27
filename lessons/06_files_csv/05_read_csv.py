import csv

with open("datasets/expenses.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = float(row["amount_eur"])
        print(row["description"], f"{amount:.2f} EUR")
