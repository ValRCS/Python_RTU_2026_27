"""Papildus: De Morgana likumi, īssavienojums un match/case.

Failam ar match/case vajadzīgs Python 3.10 vai jaunāks.
Šis nav obligāts 2. nodarbības saturs.
"""
# De Morgana likumi darbojas ar jebkādām Būla vērtībām.
a = True
b = False
kreisais = not (a and b)
labais = (not a) or (not b)
print("not (a and b):", kreisais)
print("not a or not b:", labais)
print("Rezultāti sakrīt:", kreisais == labais)

kreisais = not (a or b)
labais = (not a) and (not b)
print("not (a or b):", kreisais)
print("not a and not b:", labais)
print("Rezultāti sakrīt:", kreisais == labais)

# Izmēģini visas četras a/b kombinācijas, mainot abas vērtības.
# Īssavienojuma izpilde: ja kreisā puse ir False, labo nevērtē.
saucejs = 0
if saucejs != 0 and 10 / saucejs > 2:
    print("Dalījums ir lielāks par 2.")
else:
    print("Dalīšanu neveicām (vai rezultāts nav lielāks par 2).")

# match/case (Python 3.10+) izvēlas zaru pēc parauga.
diena = "sestdiena"
match diena:
    case "sestdiena" | "svētdiena":
        print("Brīvdiena.")
    case "pirmdiena":
        print("Jauna darba nedēļa.")
    case _:
        print("Cita diena.")
