# 5. nodarbība — papildu uzdevumi A–H

Pēc 1.–3. pamata uzdevuma izvēlies nākamo. Katram vispirms uzraksti funkciju, tad vismaz divas assert pārbaudes. [Paraugrisinājumi](bonus_solutions.py) un [testi](test_solutions.py) paredzēti pārbaudei pēc paša mēģinājuma.

| Uzdevums | Prasības un sagaidāmie rezultāti |
| --- | --- |
| A. is_even(number) | Atgriež bool; 4 → True, -3 → False, 0 → True. |
| B. is_palindrome(text) | Ignorē reģistru un tukšuma rakstzīmes, ne pieturzīmes; "Alus ari ira sula" → True, "Python" → False, "" → True. |
| C. get_statistics(numbers) | Atgriež (min, max, sum); [3, 1, 4] → (1, 4, 8); [] → None. |
| D. filter_positive(numbers) | Jauns saraksts, tikai skaitļi > 0; [-1, 0, 3, 2] → [3, 2]; [] → []; nemaina oriģinālu. |
| E. calculate_discount(price, percent=10) | Atgriež cenu pēc atlaides; 100 → 90, (80, 25) → 60. Pieņem cenu >= 0 un atlaidi 0–100. |
| F. merge_word_counts(first, second) | Jauna vārdnīca, summē sakrītošās atslēgas; {"a": 2}, {"a": 1, "b": 3} → {"a": 3, "b": 3}; avotus nemaina. |
| G. roll_dice(sides=6) | random.randint(1, sides); sides ir pozitīvs vesels skaitlis; 1 → 1, 6 → skaitlis 1–6; sides < 1 → ValueError. Testē intervālu, ne konkrētu nejaušu skaitli. |
| H. Atkļūdošana | Labo zemāk doto funkciju. [] → 0, [2, 3, 4] → 9. |

```python
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
        return total
```

Papildus: pēc izvēles pievieno docstring un tipu anotācijas. Neizmanto print return vietā. 

No repozitorija saknes:

```powershell
python exercises/05_functions_modules/bonus_solutions.py
python -m unittest discover -s exercises/05_functions_modules -p "test_*.py" -v
```

Testi pārbauda paraugrisinājumus; savu darbu pārbaudi ar analogām assert rindām savā failā.
