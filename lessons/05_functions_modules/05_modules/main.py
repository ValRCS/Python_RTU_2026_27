"""Izmanto blakus esošu moduli word_tools.py."""

import math

import word_tools


def main():
    text = "Rīga Python Rīga"
    print("Vārdu biežums:", word_tools.count_words(text))
    print("Dažādu vārdu skaits:", word_tools.unique_word_count(text))
    print("Kvadrātsakne no 81:", math.sqrt(81))


if __name__ == "__main__":
    main()
