"""Nelieli unit testi; palaišana: python -m unittest discover -s lessons/05_functions_modules/05_modules -p test_*.py -v."""

import unittest

from word_tools import count_words, unique_word_count


class WordToolsTests(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(count_words(""), {})

    def test_repeated_words_and_case(self):
        self.assertEqual(count_words("Rīga rīga PYTHON"), {"rīga": 2, "python": 1})

    def test_unique_count(self):
        self.assertEqual(unique_word_count("a b a"), 2)

    def test_punctuation_is_not_removed(self):
        self.assertEqual(count_words("rīga, rīga"), {"rīga,": 1, "rīga": 1})


if __name__ == "__main__":
    unittest.main()
