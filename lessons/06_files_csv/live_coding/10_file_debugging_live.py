import csv
import math
from pathlib import Path


def valid_amounts(path):
    valid, errors = [], []
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if not {"category", "amount_eur"} <= set(reader.fieldnames or []):
            raise ValueError("Trūkst obligātās kolonnas")
        for row in reader:
            try:
                amount = float(row["amount_eur"])
                if not math.isfinite(amount) or amount < 0 or not row["category"]:
                    raise ValueError("Nederīga summa vai kategorija")
            except (ValueError, TypeError):
                errors.append(reader.line_num)  # fiziskā beigu rinda
            else:
                valid.append(amount)
    return valid, errors


if __name__ == "__main__":
    for path in ["datasets/neeksiste.csv", "datasets/expenses_invalid.csv"]:
        try:
            valid, errors = valid_amounts(path)
        except FileNotFoundError:
            print("Nav faila:", Path(path).resolve())
        except (UnicodeDecodeError, ValueError) as error:
            print("Datu problēma:", error)
        else:
            print("Derīgi:", valid, "Kļūdu rindas:", errors)
            assert len(valid) == 2 and len(errors) == 4
