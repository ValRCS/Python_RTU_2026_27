import csv
import json
from pathlib import Path

rows = []
with open("datasets/expenses.csv", encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file):
        row["amount_eur"] = float(row["amount_eur"])
        rows.append(row)

Path("output").mkdir(exist_ok=True)
with open("output/expenses.json", "w", encoding="utf-8") as file:
    json.dump(rows, file, ensure_ascii=False, indent=2)
print("Saglabāti ieraksti:", len(rows))
