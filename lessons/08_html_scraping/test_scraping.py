import unittest
from catalog_scraper import ROOT, CATALOG, extract_products, parse_price


class ScrapingTests(unittest.TestCase):
    def test_catalog(self):
        rows = extract_products(CATALOG.read_text(encoding="utf-8"))
        self.assertEqual(len(rows), 6)
        self.assertAlmostEqual(sum(row["price"] for row in rows), 160.70)
        self.assertEqual(rows[0]["name"], "Python pamati")
        self.assertTrue(rows[0]["url"].endswith("#book-1"))

    def test_incomplete(self):
        html = (ROOT / "datasets/book_catalog_incomplete.html").read_text(encoding="utf-8")
        rows = extract_products(html)
        self.assertEqual([row["price"] for row in rows], [25.9, 32.5])

    def test_empty(self):
        self.assertEqual(extract_products("<p>Nav preču</p>"), [])

    def test_price(self):
        self.assertEqual(parse_price("32,50 €"), 32.5)
        for invalid in ["nav", "NaN", "inf", "-1"]:
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                parse_price(invalid)


if __name__ == "__main__":
    unittest.main()
