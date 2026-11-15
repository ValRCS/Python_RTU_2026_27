"""3. nodarbība: skaitļa minēšana un cilpas apstāšanās."""

secret = 7
guessed = False
maximum_attempts = 5

print("Uzmini skaitli no 1 līdz 10. Doti pieci mēģinājumi.")
for attempt in range(1, maximum_attempts + 1):
    guess = int(input(f"{attempt}. minējums: "))

    if guess == secret:
        print("Pareizi!")
        guessed = True
        break
    elif guess < secret:
        print("Par mazu.")
    else:
        print("Par lielu.")

if not guessed:
    print("Mēģinājumi beidzās; skaitlis bija", secret)

# Papildu uzdevums: pārbaudi ievades kļūdas; pilna try/except apstrāde vēlāk.
