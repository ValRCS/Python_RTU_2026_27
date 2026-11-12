# Izmēģini: ja ievadīsi nevis skaitli, bet tekstu, radīsies ValueError.
# Vēlāk kursā apgūsim, kā šo ievades kļūdu apstrādāt.
vards = input("Kā tevi sauc? ")
vecums = int(input("Cik tev ir gadu? "))

atlikušie_gadi = 100 - vecums
print(f"{vards}, pēc {atlikušie_gadi} gadiem tev būs 100 gadi.")

# Papildu uzdevums: padomā, ko programma darīs, ja vecums > 100.
