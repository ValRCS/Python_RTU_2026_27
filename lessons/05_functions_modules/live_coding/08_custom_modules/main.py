"""Palaid šo failu, lai novērotu importu un funkciju izsaukumus."""
import word_tools


def main():
    text = "Rīga Python Rīga"
    print(word_tools.count_words(text))
    print(word_tools.unique_word_count(text))


if __name__ == "__main__":
    main()
