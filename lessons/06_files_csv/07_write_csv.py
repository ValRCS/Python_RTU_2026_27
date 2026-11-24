import csv
from pathlib import Path

Path("output").mkdir(exist_ok=True)
with open("datasets/expenses.csv", encoding="utf-8", newline="") as source:
    with open("output/food.csv", "w", encoding="utf-8", newline="") as target:
        reader = csv.DictReader(source)
        writer = csv.DictWriter(target, fieldnames=["date", "category", "description", "amount_eur"])
        writer.writeheader()
        for row in reader:
            if row["category"] == "food":
                writer.writerow(row)
