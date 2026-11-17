"""Optional Week 2 demonstration of match/case (requires Python 3.10+).

For beginners: change the three values below and run this file again.
No imports or external packages are needed.
"""

# 1. The same fixed-value decision with if/elif/else and match/case.
diena = "piektdiena"  # Try "sestdiena", "pirmdiena", "otrdiena".

if diena == "sestdiena" or diena == "svētdiena":
    print("if: Brīvdiena")
elif diena == "piektdiena":
    print("if: Drīz brīvdienas!")
elif diena == "pirmdiena":
    print("if: Jauna darba nedēļa")
else:
    print("if: Cita diena")

match diena:
    case "sestdiena" | "svētdiena":
        print("match: Brīvdiena")
    case "piektdiena":
        print("match: Drīz brīvdienas!")
    case "pirmdiena":
        print("match: Jauna darba nedēļa")
    case _:
        print("match: Cita diena")

# 2. A small text menu: alternatives use |, not the Boolean word or.
komanda = " S "  # Try "quit", "help", "?".
komanda = komanda.strip().lower()  # Optional preview of string methods.

match komanda:
    case "s" | "start":
        print("Komanda: Sākam!")
    case "q" | "quit":
        print("Komanda: Beidzam.")
    case "help":
        print("Komanda: start, quit, help")
    case _:
        print("Komanda: Nezināma komanda")

# 3. input() produces a string. Literal patterns are type-sensitive here.
izvele = "1"  # This is a str, like input("Izvēle: ").
match izvele:
    case 1:
        print("Skaitlis 1")
    case "1":
        print("Virkne '1'")
    case _:
        print("Cita izvēle")
