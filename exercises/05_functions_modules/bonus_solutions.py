"""5. nodarbība — A–H paraugrisinājumi. Skaties pēc sava mēģinājuma."""
import random


def is_even(number):
    return number % 2 == 0


def is_palindrome(text):
    normalized = "".join(text.lower().split())
    return normalized == normalized[::-1]


def get_statistics(numbers):
    if not numbers:
        return None
    return min(numbers), max(numbers), sum(numbers)


def filter_positive(numbers):
    result = []
    for number in numbers:
        if number > 0:
            result.append(number)
    return result


def calculate_discount(price, percent=10):
    return price * (1 - percent / 100)


def merge_word_counts(first, second):
    merged = first.copy()
    for word, count in second.items():
        merged[word] = merged.get(word, 0) + count
    return merged


def roll_dice(sides=6):
    if sides < 1:
        raise ValueError("Kauliņam vajag vismaz vienu skaldni.")
    return random.randint(1, sides)


def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


if __name__ == "__main__":
    print(is_even(4), is_palindrome("Alus ari ira sula"))
    print(get_statistics([3, 1, 4]), filter_positive([-1, 0, 3, 2]))
    print(calculate_discount(100), merge_word_counts({"a": 2}, {"a": 1, "b": 3}))
    print(roll_dice(), sum_numbers([2, 3, 4]))
