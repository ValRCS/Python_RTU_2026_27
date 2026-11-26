import csv
from pathlib import Path


def text_stats(path):
    text = Path(path).read_text(encoding="utf-8")
    return len(text.splitlines()), len(text.split())


def safe_output(source, destination):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve() or (
        destination.exists() and source.samefile(destination)
    ):
        raise ValueError("Avots un rezultāts sakrīt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    return destination


def filter_lines(source, destination, keyword):
    destination = safe_output(source, destination)
    count = 0
    with open(source, encoding="utf-8") as src, destination.open("w", encoding="utf-8") as dst:
        for line in src:
            if keyword.lower() in line.lower():
                dst.write(line)
                count += 1
    return count


def expense_total(path):
    count, total = 0, 0.0
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            count += 1
            total += float(row["amount_eur"])
    return count, total


def expense_summary(path):
    totals = {}
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            category = row["category"]
            totals[category] = totals.get(category, 0.0) + float(row["amount_eur"])
    return totals


if __name__ == "__main__":
    print(text_stats("datasets/pilsetas.txt"))
    print(filter_lines("datasets/pilsetas.txt", "output/riga.txt", "Rīga"))
    print(expense_total("datasets/expenses.csv"))
    print(expense_summary("datasets/expenses.csv"))
