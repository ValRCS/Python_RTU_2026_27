import csv

totals = {}
count = 0
total = 0.0
with open("datasets/expenses.csv", encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file):
        amount = float(row["amount_eur"])
        category = row["category"]
        count += 1
        total += amount
        totals[category] = totals.get(category, 0.0) + amount
        print(count, category, f"{total:.2f}")
print(f"Kopā {count}: {total:.2f} EUR")
for category, amount in sorted(totals.items()):
    print(category, f"{amount:.2f}")
assert count == 10
assert abs(total - 35) < 1e-9
