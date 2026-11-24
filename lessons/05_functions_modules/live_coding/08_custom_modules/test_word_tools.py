"""Palaid: python -m unittest discover -s lessons/05_functions_modules/live_coding/08_custom_modules -v"""
import unittest
from word_tools import count_words, unique_word_count


class WordToolsTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_words(""), {})

    def test_repeat(self):
        self.assertEqual(count_words("Rīga rīga"), {"rīga": 2})

    def test_unique(self):
        self.assertEqual(unique_word_count("a b a"), 2)


if __name__ == "__main__":
    unittest.main()
