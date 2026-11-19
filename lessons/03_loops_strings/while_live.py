print("Valdis runājā")
print("Valdis runājā")
print("Valdis runājā")
print("Valdis runājā")
print("Valdis runājā")
print("Valdis runājā")
# ko tad darīt ja vajag 100 vai teiksim miljons reize atkārtoties

# ar while ciklu mēs daram kaut ko kamēr kaut kāds nosacījums ir True

# while True:
#     print("skrienu")
#     print("lecu")
#     print("atpūšos")
#     print("Velu akmeni augšā")
#     print("One must imagine Sysiphus happy")
# mūžīgie cikli var būt noderīgi ja ir iespēja tos apstādīnāt ar specialu komandu break nedaudz vēlāk

print("Tūliņ sāksim ciklu")

count = 0  # izdomājam mainīgo un inicializējam ar kādu vērtību
while count < 5: # pārbaudam nosacījumu 
    # šeit izpildam ja count < 5
    print("Skrienu")
    print(f"Count ir {count}")
    count+=1 # tas pats kas count = count + 1  # ir valodas kur to dara ar count++
    # atgriežam atkal pārbaudīt count < 5
# te jau esam ārā no cikla
print(f"Count vērtība pēc cikla ir {count}")
print("Esam ārā no cikla")

# mēs varam arī iet lejā
floor = 9 # to 
while floor >= 0:
    print(f"Laižam lejup, esam stāvā {floor}")
    # kritiski ir nomainīt stāvu uz leju šeit!
    floor -= 1 # tas pats kas floor = floor - 1

# esam ārā no cikla
print(f"Esam nolaidušies, stāvs ir {floor}")

# product = 1  # Vai 0 derētu? :)
# while product < 1_000: # 1_000 ir tas pats kas 1000 Python sintakse
#     print(f"Patlaban reizinājums ir {product}")
#     skaitlis = int(input("Lūdzu ievadiet veselu skaitli: "))
#     product *= skaitlis # tas pats kas product = product * skaitlis

# # esam ārpusē tatad product ir >= 1_000 vismaz tūkstoties
# print(f"Reizinājums ir cikla ārpusē tagad {product}")

# varam tagad izveidot vispārinātu risinājumu
START = 100  # lieliem burtiem ir parasti mainīgi, lai gan labais stils teikti tie būs nemainīgi
# END = 200_000
END = 200
STEP = 30

i = START # inicializācija
while i < END: # varētu būt ari i <= END atkarigs vai END ir iekļaujošs
    print(f"Kaut ko daram ar i {i}")
    # mainam i
    i += STEP # tas pats kas i = i + STEP

print(f"Ārpusē i ir {i} pēc cikla beigām")

# mēs varam pārbaudīt arī divus vai vairāk nosacījumus
is_job_active = True # tipisks gājiens ar karodziņu
job_count = 0
MAX_JOBS = 10 # tā sauktais circuit_breakers
while is_job_active and job_count < MAX_JOBS:
    print(f"kaut ko daram ar job count No. {job_count}")
    # šeit tas uzdevums varētu turpināties
    # te varētu būt jebkādas instrukcijam šim darbam
    job_count += 1
    # es pieprasu lietotāja ievadi
    user_input = input("vai esi beidzis ievadi j lai beigtu ")
    if user_input == "j": # šis nav pārāk draudzīgs variants jo tikai j uzreiz beigs, Y vai J nestrādās
        is_job_active = False # nomainam karodziņa vērtību
    # ejam uz cikla sākumu rindiņa 69 un pārbaudam atkal

# esam ārā
print(f"Ārpusē ir job_count {job_count} un karodziņš is_job_active {is_job_active}")