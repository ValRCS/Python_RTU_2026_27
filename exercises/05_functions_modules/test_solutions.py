"""Regresijas testi A–H paraugrisinājumiem."""
import unittest
from bonus_solutions import (
    is_even, is_palindrome, get_statistics, filter_positive,
    calculate_discount, merge_word_counts, roll_dice, sum_numbers,
)


class BonusTests(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-3))

    def test_palindrome(self):
        self.assertTrue(is_palindrome("Alus ari ira sula"))
        self.assertFalse(is_palindrome("Python"))
        self.assertTrue(is_palindrome(""))

    def test_statistics(self):
        self.assertEqual(get_statistics([3, 1, 4]), (1, 4, 8))
        self.assertIsNone(get_statistics([]))

    def test_filter(self):
        original = [-1, 0, 3, 2]
        self.assertEqual(filter_positive(original), [3, 2])
        self.assertEqual(original, [-1, 0, 3, 2])
        self.assertEqual(filter_positive([]), [])

    def test_discount(self):
        self.assertAlmostEqual(calculate_discount(100), 90)
        self.assertAlmostEqual(calculate_discount(80, 25), 60)

    def test_merge(self):
        first, second = {"a": 2}, {"a": 1, "b": 3}
        self.assertEqual(merge_word_counts(first, second), {"a": 3, "b": 3})
        self.assertEqual(first, {"a": 2})
        self.assertEqual(second, {"a": 1, "b": 3})

    def test_dice(self):
        self.assertEqual(roll_dice(1), 1)
        for _ in range(20):
            self.assertIn(roll_dice(), range(1, 7))
        with self.assertRaises(ValueError):
            roll_dice(0)

    def test_sum(self):
        self.assertEqual(sum_numbers([]), 0)
        self.assertEqual(sum_numbers([2, 3, 4]), 9)


if __name__ == "__main__":
    unittest.main()
