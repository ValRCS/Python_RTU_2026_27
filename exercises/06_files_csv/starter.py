"""Aizpildi funkcijas pēc kārtas; palaid no repozitorija saknes."""
import csv
from pathlib import Path


def text_stats(path):
    # TODO: atgriez (rindu skaits, vārdu skaits).
    raise NotImplementedError


def filter_lines(source, destination, keyword):
    # TODO: pārbaudi ceļus, izveido mapi, atgriez atlasīto skaitu.
    raise NotImplementedError


def expense_total(path):
    # TODO: atgriez (ierakstu skaits, summa).
    raise NotImplementedError


def expense_summary(path):
    # TODO: atgriez kategoriju vārdnīcu.
    raise NotImplementedError


if __name__ == "__main__":
    # Atkomentē pārbaudi pēc funkcijas pabeigšanas.
    # print(text_stats("datasets/pilsetas.txt"))  # (5, 5)
    # print(filter_lines("datasets/pilsetas.txt", "output/riga.txt", "Rīga"))  # 2
    # print(expense_total("datasets/expenses.csv"))  # (10, 35.0)
    # print(expense_summary("datasets/expenses.csv"))
    print("Aizpildi funkciju un atkomentē pārbaudi.")
