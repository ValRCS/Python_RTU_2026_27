# let's make a game of guess the number one user enters secret number
# second user tries to guess it
# we can use password input to hide the secret number


# import getpass # ar šo mēs varam noslēpt ievadu, nerādot to ekrānā

# secret_number = int(getpass.getpass("Ievadi slepeno skaitli: "))
# # TODO add input validation to make sure secret number is an integer

# varam arī likt datoram izvēlēties slepeno skaitli
import random # random nāk līdzi Python bet tas ir jāimportē, lai varētu izmantot

secret_number = random.randint(1, 100)

# now second player starts
MAX_TRIES = 7 # ar 7 var atrast skaitļos no 1 līdz 128 jo 2**7 = 128, bet mēs varam arī palielināt līdz 10
tries = 0
while True:
    print(f"Mēģinājums {tries + 1} no {MAX_TRIES}")
    try:
        guess = int(input("Uzmini slepeno skaitli: "))
    except ValueError:
        print("Lūdzu, ievadiet derīgu skaitli.")
        continue # nav vesels skaitlis, lēksim atpakaļ uz sākumu ciklam 14 rindiņu
    if guess < secret_number:
        print("Skaitlis ir lielāks")
    elif guess > secret_number:
        print("Skaitlis ir mazāks")
    else:
        print("Apsveicu! Uzminēji slepeno skaitli!")
        break # iziet no cikla, jo uzminēja
    tries += 1
    if tries >= MAX_TRIES:
        print("Diemžēl neuzminēji slepeno skaitli, Zaudēji")
        break # iziet no cikla, jo beidzās mēģinājumi