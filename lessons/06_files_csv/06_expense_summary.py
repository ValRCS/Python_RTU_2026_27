import csv

def expense_summary(path):
    totals = {}
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            category = row["category"]
            amount = float(row["amount_eur"])
            totals[category] = totals.get(category, 0.0) + amount
    return totals

if __name__ == "__main__":
    totals = expense_summary("datasets/expenses.csv")
    for category, amount in sorted(totals.items()):
        print(f"{category}: {amount:.2f} EUR")
    print(f"Kopā: {sum(totals.values()):.2f} EUR")
    assert abs(sum(totals.values()) - 35.0) < 1e-9
