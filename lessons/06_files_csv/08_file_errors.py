import csv
import math

try:
    with open("datasets/expenses.csv", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if "amount_eur" not in (reader.fieldnames or []):
            raise ValueError("Trūkst amount_eur kolonnas")
        for row in reader:
            try:
                amount = float(row["amount_eur"])
                if not math.isfinite(amount) or amount < 0:
                    raise ValueError("Nederīga summa")
                print(amount)
            except (ValueError, TypeError):
                print(f"Nederīgs ieraksts, beigu rinda {reader.line_num}.")
except FileNotFoundError:
    print("Fails nav atrasts. Pārbaudi darba mapi.")
except UnicodeDecodeError:
    print("Pārbaudi faila kodējumu.")
except ValueError as error:
    print(error)
