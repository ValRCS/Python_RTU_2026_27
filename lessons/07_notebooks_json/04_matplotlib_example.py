import json
import matplotlib.pyplot as plt

with open("datasets/expenses.json", encoding="utf-8") as file:
    expenses = json.load(file)
totals = {}
for row in expenses:
    category = row["category"]
    totals[category] = totals.get(category, 0.0) + row["amount_eur"]

plt.bar(list(totals), list(totals.values()))
plt.title("Izdevumi pa kategorijām")
plt.ylabel("EUR")
plt.tight_layout()
plt.show()
