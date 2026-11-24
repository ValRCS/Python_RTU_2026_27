import json
from pathlib import Path

with open("datasets/expenses.json", encoding="utf-8") as file:
    expenses = json.load(file)

food = []
for row in expenses:
    if row["category"] == "food":
        food.append(row)

Path("output").mkdir(exist_ok=True)
with open("output/food.json", "w", encoding="utf-8") as file:
    json.dump(food, file, ensure_ascii=False, indent=2)
print(f"Pārtika: {sum(row['amount_eur'] for row in food):.2f} EUR")
