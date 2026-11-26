import csv
import math
import string
from decimal import Decimal
from pathlib import Path
from solutions import expense_summary, expense_total, filter_lines, safe_output, text_stats


def top_words(path, limit=10):
    counts = {}
    for word in Path(path).read_text(encoding="utf-8").lower().split():
        word = word.strip(string.punctuation + "…–—“”„")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def clean_text(source, destination):
    destination = safe_output(source, destination)
    lines = []
    for line in Path(source).read_text(encoding="utf-8").splitlines():
        line = line.translate(str.maketrans("", "", string.punctuation + "…–—“”„")).strip()
        if line:
            lines.append(line)
    destination.write_text("".join(line + "\n" for line in lines), encoding="utf-8")
    return len(lines)


def export_category(source, destination, category):
    destination = safe_output(source, destination)
    count = 0
    with open(source, encoding="utf-8", newline="") as src:
        reader = csv.DictReader(src)
        with destination.open("w", encoding="utf-8", newline="") as dst:
            writer = csv.DictWriter(dst, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                if row["category"] == category:
                    writer.writerow(row)
                    count += 1
    return count


def sales_total(path):
    count, total = 0, Decimal("0")
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            total += int(row["quantity"]) * Decimal(row["unit_price"])
            count += 1
    return count, total


def export_summary(source, destination):
    destination = safe_output(source, destination)
    totals = expense_summary(source)
    with destination.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["category", "amount_eur"])
        for category, amount in sorted(totals.items()):
            writer.writerow([category, f"{amount:.2f}"])
    return len(totals)


def batch_filter(source_folder, destination_folder):
    result = {}
    for path in sorted(Path(source_folder).glob("*.txt")):
        result[path.name] = filter_lines(path, Path(destination_folder) / path.name, "Rīga")
    return result


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


def regional_total(path):
    total = Decimal("0")
    with open(path, encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file, delimiter=";"):
            total += int(row["daudzums"]) * Decimal(row["cena"].replace(",", "."))
    return total


def decimal_total(path):
    with open(path, encoding="utf-8", newline="") as file:
        return sum((Decimal(row["amount_eur"]) for row in csv.DictReader(file)), Decimal("0"))


def report(source, destination):
    destination = safe_output(source, destination)
    count, total = expense_total(source)
    lines = [f"Ieraksti: {count}", f"Kopā: {total:.2f} EUR"]
    for category, amount in sorted(expense_summary(source).items()):
        lines.append(f"{category}: {amount:.2f} EUR")
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    out = Path("output/lesson06/bonus")
    print("6.5", top_words("datasets/rainis.txt"))
    print("6.6", clean_text("datasets/veidenbaums.txt", out / "clean.txt"))
    print("6.7", export_category("datasets/expenses.csv", out / "food.csv", "food"))
    print("6.8", sales_total("datasets/sales.csv"))
    print("6.9", export_summary("datasets/expenses.csv", out / "summary.csv"))
    print("6.10", batch_filter("datasets/sample_texts", out / "batch"))
    print("6.11", valid_amounts("datasets/expenses_invalid.csv"))
    print("6.12", regional_total("datasets/products_lv.csv"))
    print("6.13", decimal_total("datasets/expenses.csv"))
    assert text_stats("datasets/pilsetas.txt") == (5, 5)
    report("datasets/expenses.csv", out / "report.txt")
