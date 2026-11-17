# Instructor supplement — Week 2 `match/case` bonus

**Lesson:** 2 — Boolean logic and branching (17 November 2026)  
**Audience:** instructor; this is *optional enrichment*, not a required learning outcome.  
**Prerequisite:** students can already use `if/elif/else` and distinguish `str` from `int`.  
**Runtime:** **Python 3.10+**; no third-party packages.  
**Links:** [main teaching plan](2026-11-17_lesson02_instructor_plan.md) · [student bonus section](../docs/lessons/02-types-conditions/index.html#papildus) · [runnable demo](../lessons/02_types_conditions/08_match_case_bonus.py) · [existing logic bonus](../lessons/02_types_conditions/07_bonus_logic.py).

## Instructional intent

This is a **short optional closing segment**, not a replacement for the lesson's central `if/elif/else` work. Teach a modest claim: if several branches check **one value against known literal alternatives**, `match/case` can read more naturally. The name *structural pattern matching* matters because Python's feature is more powerful than a conventional switch statement, but teaching sequences, mappings and class patterns belongs **after** the foundations (especially Week 4 collections).

**Decision rule:** prioritize the scheduled 21:30–21:40 recap and transition to loops. If the class needs debugging time, skip the bonus without penalty. For a group that has finished early, use this supplement.

## 10-minute teaching route (21:30–21:40; flexible)

| Time | Instructor action | Student checkpoint |
| --- | --- | --- |
| 0–2 min | Recall the already-familiar weekday `if/elif/else` example; ask when several checks depend on the same variable. | Identify `diena` as the value being compared. |
| 2–5 min | Run `08_match_case_bonus.py`; show literal `case`, the `|` alternative, and `case _`. | Predict `piektdiena` and `sestdiena` outputs. |
| 5–7 min | Change `komanda` from `" S "` to `"quit"` and `"?"`. | Explain why `|` here means alternative **patterns**, not Boolean `or`. |
| 7–9 min | Show `izvele = "1"`; compare `case 1` with `case "1"`. | Explain why input text does not match integer literal `1`. |
| 9–10 min | Ask when `if` remains preferable; reaffirm Python 3.10+ and that this topic is optional. | Answer: ranges and general Boolean conditions usually still use `if`. |

**Suggested instructor wording (English):** “We are not replacing `if`. Think of `match` as inspecting one value against a series of *patterns*. Today the patterns are just fixed values, so it looks like a switch statement. Later, Python can match shapes of data as well.”

**Suggested short Latvian wording:** “`match/case` pārbauda vienu vērtību pret vairākiem paraugiem. Šodien izmantojam vienkāršus tekstu paraugus; intervāliem un saliktiem loģiskiem nosacījumiem joprojām lietojam `if`.”

## Working example and anticipated output

From the repository root:

```text
python --version
python lessons/02_types_conditions/08_match_case_bonus.py
```

Use `python3` on macOS/Linux or `py` when appropriate on Windows. Confirm the reported interpreter is at least 3.10 **before** running: an earlier version fails to parse the `match` syntax.

Default output:

```text
if: Drīz brīvdienas!
match: Drīz brīvdienas!
Komanda: Sākam!
Virkne '1'
```

The script deliberately uses assignments, not loops or custom functions: students have not formally learned those yet. Its `.strip().lower()` line is only a preview of Week 3 string methods; do not spend the bonus teaching them in depth. Change `diena`, `komanda` and `izvele` in the file and rerun.

### Core syntax and semantics to emphasize

```python
match diena:
    case "sestdiena" | "svētdiena":
        print("Brīvdiena")
    case "piektdiena":
        print("Drīz brīvdienas!")
    case _:
        print("Cita diena")
```

- `match diena:` evaluates a subject expression, then considers case patterns **in order**. After the first successful case, execution continues **after** the match statement; there is **no C-style fall-through** and no required `break`.
- Literal `case "piektdiena":` matches that value; `case "sestdiena" | "svētdiena":` represents **alternative patterns**. It is **not** the expression `"sestdiena" or "svētdiena"`.
- `case _:` is a wildcard / default case. It binds no variable, is optional, and must be last when included unguarded. Without a matching case and without a wildcard, no case body runs.
- The same `if/elif/else` may be **better** when testing `vecums >= 18 and vecums < 65` or unrelated Boolean expressions. Do not suggest `match` is universally more concise.
- Matching string literals is case-sensitive. When the value comes from `input()`, it is `str`; `case 1:` will not match the text `"1"`. Convert the input before matching if the program is meant to match numeric literals.

### Important trap: a bare name is a *capture*, not a comparison

Do **not** present the following as working code with two alternatives:

```python
# INCORRECT: 'piektdiena' here is a capture variable, not a named constant.
match diena:
    case piektdiena:
        print("Matches anything and assigns to piektdiena!")
    case _:
        print("Unreachable")  # SyntaxError: irrefutable preceding case
```

To match a **literal string**, use `case "piektdiena":`. A bare name inside a pattern normally captures/binds a value; it does not compare to an existing variable. This is a frequent source of misconception. A qualified constant like `Color.RED` is a distinct, later-level *value pattern*; there is no need to teach that now.

## Optional extension for 10–20 additional minutes (only if class time permits)

1. **Side-by-side rewrite (4 min).** Ask students to turn the weekday `if/elif/else` example into a `match`. Preserve identical output and include `case _`.
2. **Small text menu (4 min).** Add a command alias using `|`, e.g. `case "h" | "help":`, and test an unexpected input. Point out that case order and the default matter.
3. **Formative debugging (2–4 min).** Put `case _:` before a literal branch (ask why it fails), or replace `case "start":` with `case start:` (ask whether it compares a variable).
4. **Advanced *instructor-only* preview (3–5 min).** If students are clearly ready, demonstrate a *guard* and a structural pattern. These require concepts beyond the essential Week 2 lesson:

```python
# Guard: use a Boolean condition only after a literal pattern has matched.
command = "help"
allowed = True
match command:
    case "help" if allowed:
        print("Showing help")
    case "help":
        print("Help is disabled")
    case _:
        print("Unknown command")

# Structural example, best saved for Week 4 (sequences/collections).
message = ["move", "north"]
match message:
    case ["move", "north" | "south"]:
        print("Vertical movement")
    case ["move", direction]:
        print("Other direction:", direction)  # 'direction' captures the element
    case _:
        print("Not a movement command")
```

**Framing of advanced preview:** a `guard` is an additional `if` test after a pattern matches; a sequence pattern checks shape and parts of data rather than merely comparing the whole value. Do **not** turn this into a full treatment of nested patterns, dictionary matching, `as`, or class matching during the Week 2 lesson.

## Check-for-understanding questions (with expected answers)

| Prompt | Expected answer |
| --- | --- |
| What prints for `diena = "svētdiena"`? | Both `if` and `match` print `Brīvdiena`. |
| Is `case "a" or "b":` the right way to express two alternatives? | No; use `case "a" \| "b":`. |
| What happens without `case _:` for an unknown command? | No matching case body executes; control continues after `match`. |
| Does `case 1:` match the `"1"` returned by `input()`? | No; the input is text unless explicitly converted. |
| Why not rewrite `if vecums >= 18:` as `case >= 18:`? | `case >= 18` is invalid pattern syntax. Use `if` for arbitrary comparisons; guards are possible but do not make this a good match use case. |

## Teaching risks and fallback

- **Do not overload:** if students are still resolving indentation, `elif` order, or `input()` conversion, prioritize those outcomes. Treat the bonus as optional self-study via the HTML lesson and `07_bonus_logic.py`.
- **No wrong analogy:** “like switch/case” is an entry point, not a complete definition. Python has no implicit fall-through; `match` is a statement using patterns, not arbitrary Boolean cases.
- **No typing surprise:** `match` requires Python 3.10+. `match` and `case` are soft keywords; demonstrate them only in the intended syntax.
- **No false distinction:** `|` between patterns is **not** bitwise OR applied to two strings and is **not** a Python `or` Boolean expression.
- **No prerequisite drift:** save collection structure examples and capture-variable depth for Week 4 or optional advanced exploration.

## References and provenance

- [Python tutorial: `match` statements](https://docs.python.org/3/tutorial/controlflow.html#match-statements) — approachable syntax and first examples.
- [PEP 636 — Structural Pattern Matching Tutorial](https://peps.python.org/pep-0636/) — examples, guards, capture patterns, and deeper structural matching.
- [Python language reference: the `match` statement](https://docs.python.org/3/reference/compound_stmts.html#the-match-statement) — authoritative syntax and semantics.
- [Python 3.10 release notes](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching) — introduction and motivation.
- [2024/25 predecessor example](https://github.com/ValRCS/Python_RTU_2024_25/blob/main/topic_3_booleans_logic_branching/pattern_matching.py) — simple numeric dispatch, adapted rather than copied wholesale.

**Validation:** run `python -m py_compile lessons/02_types_conditions/08_match_case_bonus.py` with Python 3.10+, execute the script, and check the four default output lines above. The teaching notes are in English so they can be reused in later cohorts; student examples remain in Latvian.
