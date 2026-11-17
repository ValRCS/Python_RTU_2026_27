# mēs varam izmantot Booleanus lai veiktu izvēli ko datoram darīt
# is_warm = False
is_warm = True
# ar if mēs varam veikt izvēli
if is_warm: # lai izpildītu nākošas rindiņas is_warm jabūt truthy - patiesīgam, šeit True derētu bet False neder
    print("Iesim peldēties!")
    print("Pēc tam ēdisim saldējumu!")
    # tehniski vēl esam if blokā, kurš izpildā tikai tad kad is_warm ir patiess - True
    print("Un tad sauļosimies!")
# tikko ejom nost no atkāpes atgriežas normālajā globalājā izpildes blokā
# nākošā rindiņa vienmēr izpildīsies
print("Esam mājās!")

# var būt arī tā ka mums ir viens no diviem ceļiem kurus vēlamies izvēlētis
# tas ir viens vai otrs, bet ne abi, un neviens arī neder
# analoģija ar diviem ceļiem kas zarojās un tad saiet kopā

current_temp = 5 + 30
hot_temp = 25

if current_temp < hot_temp:
    print("Nav tik karsts...")
    print(f"{current_temp} ir mazāks par {hot_temp} un līdz ar to nelienam āra")
else: # tātad tas nozimē current_temp >= hot_temp pēc izslēgšanas metodes
    print("Karstumiņš")
    print(f"{current_temp} ir vienāds vai lielāks par {hot_temp} un līdz ar to ejam priecāties")

# Esam āra no if else blokiem un abi ceļie ir atpakaļ vienā
print("Darbojamies tālāk neatkarīgi no temperatūrām")

# kā būt ar tris ceļiem, no kuriem izpildās tikai viens?
print("*"*40) # atdalītājs

secret_number = 42 #noslēpums varēja arī nākt no citurienes nevis lokāli
print("Uzminiet manu skaitli!")
guess = int(input("Kāds ir jūsu minējums?")) # šo ievada lietotājs
# int tāpēc ka input vienmēr dod string

if guess > secret_number:
    print(f"Jūsu minējums {guess} ir par lielu")
elif guess < secret_number:
    print(f"Jūsu minējums {guess} ir par mazu :(")
else: # nozimē ka par lielu un par mazu abi bija nepatiesi, # tātad abi mainīgiem vienādi
    # tātad uzminēts!
    print(f"Malači! Jūsu {guess} ir vienāds ar slepeno {secret_number}")

print("Programmas beigas")