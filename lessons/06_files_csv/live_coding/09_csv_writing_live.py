import csv
from pathlib import Path

output = Path("output/lesson06")
output.mkdir(parents=True, exist_ok=True)
with open("datasets/expenses.csv", encoding="utf-8", newline="") as src:
    reader = csv.DictReader(src)
    with (output / "food.csv").open("w", encoding="utf-8", newline="") as dst:
        writer = csv.DictWriter(dst, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if row["category"] == "food":
                writer.writerow(row)
with (output / "food.csv").open(encoding="utf-8", newline="") as file:
    assert len(list(csv.DictReader(file))) == 5
with (output / "example.csv").open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["prece", "cena"])
    writer.writerow(["maize, rupjā", 2.15])
