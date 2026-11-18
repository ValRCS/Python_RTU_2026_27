# Instructor supplement — Lesson 3: error handling in loops

**Date:** 19 November 2026  
**Role:** optional extension after the 15-minute mandatory input-validation demonstration.  
**Resources:** [main instructor schedule](2026-11-19_lesson03_instructor_plan.md) · [student HTML](../docs/lessons/03-loops-strings/index.html#kludas) · [runnable demo](../lessons/03_loops_strings/05_error_handling.py) · [practice sheet](../exercises/03_loops_strings/README.md).

## Core live coding: 15 minutes

Run `python lessons/03_loops_strings/05_error_handling.py` (or `python3` on macOS/Linux). Type `abc` → `-2` → `5` in sequence.

- **Type conversion:** `int("abc")` raises `ValueError`, caught by `except ValueError`. Then `continue` requests fresh input.
- **Domain validation:** `int("-2")` succeeds, but `number < 0` is true. This is not an exception: use `if`.
- **Success:** `5` passes both checks and `break` exits the loop. The final `print` can safely use `number`.

Have students predict which path executes before each input. The contrast between an exception and a valid value that violates application rules is more important than memorizing every exception type.

**Teaching boundary:** avoid generalized `except:`, custom exceptions, `else`/`finally` and abstractions using `def` (scheduled for lesson 5). Do not let the bonus displace 20:25–21:05 independent practice.

## Optional extension A — quit command (5 minutes)

Open the collapsed `q` example in the student HTML page. Demonstrate `q`, `Q`, `  Q  `, `3`, and `hello`. Explain why checking the quit command **before** `int(text)` matters. Compare `break` (finish) with `continue` (retry). The program can accept multiple numbers before exiting.

## Optional extension B — two exception classes (5 minutes)

Open the collapsed division example. Contrast `float("abc")` → `ValueError` and `3 / 0` → `ZeroDivisionError`. Catch each with its own handler, without implying the program catches every possible failure. A `KeyboardInterrupt` from Ctrl+C remains outside this example intentionally.

## Challenging extension — five *valid* guesses

The basic exercise uses `for range(1, 6)` and accepts the possibility of invalid conversion ending the program. In the advanced version, do not consume an attempt for invalid text or guesses outside 1–10:

```python
secret = 7
attempts = 0
guessed = False

while attempts < 5:
    text = input("Minējums no 1 līdz 10: ")
    try:
        guess = int(text)
    except ValueError:
        print("Ievadi veselu skaitli.")
        continue

    if not 1 <= guess <= 10:
        print("Skaitlim jābūt no 1 līdz 10.")
        continue

    attempts += 1
    if guess == secret:
        guessed = True
        print("Pareizi!")
        break
    elif guess < secret:
        print("Par mazu")
    else:
        print("Par lielu")

if not guessed:
    print("Pieci derīgi mēģinājumi izmantoti.")
```

Suggested test: `abc` → `0` → `4` → `7`. Only `4` and `7` use an attempt. Another test should use five wrong numbers inside 1–10.

### Anticipated questions

- **Why use `continue`?** It makes the retry explicit and ensures subsequent code does not accidentally use an undefined or invalid value.
- **Does `except ValueError` reject negative integers?** No. `-2` parses correctly; reject with `if` where required.
- **Does `break` stop an `if` branch?** No. It stops the nearest enclosing loop.
- **Why not `str.isdigit()`?** It is not a complete integer parser; `"-2".isdigit()` is false even though `int("-2")` works.
- **What about `except Exception` or bare `except`?** They are too broad for this beginner input-conversion case and risk hiding unexpected errors.

## Reviewed previous-year references

- [2024/25 input retry](https://github.com/ValRCS/Python_RTU_2024_25/blob/main/topic_4_loops_and_errors/error_handling_m27.py) — useful pattern, but contains an uncommented prose line, so **do not run verbatim**.
- [2024/25 friendly input](https://github.com/ValRCS/Python_RTU_2024_25/blob/main/topic_5_strings/friendly_user_input.py) — optional exit command.
- [2024/25 error types](https://github.com/ValRCS/Python_RTU_2024_25/blob/main/topic_4_loops_and_errors/error_handling_m26.py) — optional second exception class.
- [Official Python tutorial: Handling Exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions).

**Fallback:** when students struggle with indentation, show just `while True` plus `except ValueError` and postpone both optional extensions.
