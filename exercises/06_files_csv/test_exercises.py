import csv
import unittest
from decimal import Decimal
from pathlib import Path
from tempfile import TemporaryDirectory
from solutions import text_stats, filter_lines, expense_total, expense_summary
from bonus_solutions import (top_words, clean_text, export_category, sales_total,
                             export_summary, batch_filter, valid_amounts,
                             regional_total, decimal_total, report)

DATA = Path(__file__).resolve().parents[2] / "datasets"


class FileExercises(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.out = Path(self.temp.name)

    def test_text_stats(self):
        self.assertEqual(text_stats(DATA / "pilsetas.txt"), (5, 5))
        empty = self.out / "empty.txt"
        empty.touch()
        self.assertEqual(text_stats(empty), (0, 0))

    def test_filter(self):
        dest = self.out / "nested" / "riga.txt"
        self.assertEqual(filter_lines(DATA / "pilsetas.txt", dest, "RĪGA"), 2)
        self.assertEqual(dest.read_text(encoding="utf-8").splitlines(), ["Rīga", "Rīga"])

    def test_same_path(self):
        path = self.out / "source.txt"
        path.write_text("Rīga", encoding="utf-8")
        with self.assertRaises(ValueError):
            filter_lines(path, path, "Rīga")
        self.assertEqual(path.read_text(encoding="utf-8"), "Rīga")

    def test_total(self):
        count, total = expense_total(DATA / "expenses.csv")
        self.assertEqual(count, 10)
        self.assertAlmostEqual(total, 35.0)

    def test_summary(self):
        totals = expense_summary(DATA / "expenses.csv")
        expected = {"food": 13.50, "transport": 3.0, "books": 15.60, "household": 2.90}
        self.assertEqual(totals.keys(), expected.keys())
        for key in totals:
            self.assertAlmostEqual(totals[key], expected[key])

    def test_words(self):
        self.assertEqual(top_words(DATA / "pilsetas.txt")[0], ("rīga", 2))

    def test_clean(self):
        src = self.out / "src.txt"
        src.write_text("Rīga!\n\nCēsis…\n", encoding="utf-8")
        dest = self.out / "clean.txt"
        self.assertEqual(clean_text(src, dest), 2)
        self.assertEqual(dest.read_text(encoding="utf-8"), "Rīga\nCēsis\n")

    def test_csv_export(self):
        dest = self.out / "food.csv"
        self.assertEqual(export_category(DATA / "expenses.csv", dest, "food"), 5)
        with dest.open(encoding="utf-8", newline="") as file:
            rows = list(csv.DictReader(file))
            self.assertEqual(len(rows), 5)
            self.assertTrue(all(row["category"] == "food" for row in rows))

    def test_sales(self):
        self.assertEqual(sales_total(DATA / "sales.csv"), (60, Decimal("372.00")))

    def test_export_summary(self):
        self.assertEqual(export_summary(DATA / "expenses.csv", self.out / "summary.csv"), 4)

    def test_batch(self):
        self.assertEqual(batch_filter(DATA / "sample_texts", self.out / "batch"), {"01.txt": 2, "02.txt": 1})

    def test_invalid(self):
        valid, errors = valid_amounts(DATA / "expenses_invalid.csv")
        self.assertEqual(valid, [2.15, 3.60])
        self.assertEqual(errors, [3, 4, 5, 6])

    def test_missing_header(self):
        path = self.out / "bad.csv"
        path.write_text("wrong\n1\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            valid_amounts(path)

    def test_regional_and_decimal(self):
        self.assertEqual(regional_total(DATA / "products_lv.csv"), Decimal("10.60"))
        self.assertEqual(decimal_total(DATA / "expenses.csv"), Decimal("35.00"))

    def test_report(self):
        dest = self.out / "report.txt"
        report(DATA / "expenses.csv", dest)
        self.assertIn("Kopā: 35.00 EUR", dest.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
