import csv

try:
    with open("datasets/expenses.csv", encoding="utf-8", newline="") as file:
        for line_number, row in enumerate(csv.DictReader(file), start=2):
            try:
                print(float(row["amount_eur"]))
            except (ValueError, TypeError, KeyError):
                print(f"Nederīgs ieraksts {line_number}. rindā.")
except FileNotFoundError:
    print("Fails nav atrasts. Pārbaudi darba mapi.")
except UnicodeDecodeError:
    print("Pārbaudi faila kodējumu.")
