# Ievadi nenegatīvu n un ar for/range aprēķini summu no 1 līdz n. 
# Pārbaudi n=0 → 0, n=1 → 1, n=10 → 55.
#  Papildus: pāra skaitļu summa un kļūdainas ievades atkārtošana.

# vispirms iegūstam n no lietotāja, pārbaudām vai tas ir nenegatīvs skaitlis
while True:
    n = input("Ievadi nenegatīvu n: ")
    try:
        n = int(n)
        # šeit zinam ka mums ir vesels skaitlis, bet varbūt tas ir negatīvs
        if n < 0:
            print("Ievadītais skaitlis ir negatīvs, mēģini vēlreiz.")
            continue # leksim atpakaļ uz sākumu ciklam, lai lietotājs varētu ievadīt jaunu skaitli
        # šajā vietā zinam ka n ir nenegatīvs skaitlis, varam iziet no cikla
        break # tas lec ārā uz 20 rindiņu
    except ValueError:
        print("Kļūda! Ievadi nenegatīvu skaitli.")
        continue # lieks jo cikls tāpat turpinās, bet var būt skaidrāk lietot continue

print("Esam ārā no ievades cikla, n ir", n)
# Aprēķinām summu no 1 līdz n
total_sum = 0
for i in range(1, n + 1): # tātad ja n ir 0 tad nekas nenotiks jo range(1, 1) ir tukšs
    total_sum += i

summa = 0
# drukasim katru summu izmanotojo sum kā studentes piemērā
for i in range(1, n + 1):
    summa = sum(range(1, i + 1)) # šeit varētu arī izmantot summu += i bet šeit mācāmies range
    print(f"Summa no 1 līdz {i} ir {summa}")

print(f"Summa no 1 līdz {n} ir {total_sum}")
# varēja jau izmanot summa = sum(range(1, n + 1)) bet šeit mācāmies ciklus un range

# Aprēķinām pāra skaitļu summu no 1 līdz n
even_sum = 0
for i in range(2, n + 1, 2): # tas pa ja n ir 0 vai 1 tad šis range būs tukšs un nekas nenotiks
    even_sum += i

print(f"Pāra skaitļu summa no 1 līdz {n} ir {even_sum}")