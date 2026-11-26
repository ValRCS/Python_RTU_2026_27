# python ir ļoti plaša standarta bibliotēka, kas satur daudz dažādu moduļu, kurus mēs varam izmantot savos projektos

# populāra ir https://docs.python.org/3/library/datetime.html
# tad nav pašam jāraksta datuma un laika funkcijas, bet var izmantot jau gatavas

# piemērs
from datetime import datetime
import sys # šeit mēs importējam tikai datetime klasi no datetime moduļa, jo tas ir modulī ar tādu pašu nosaukumu
now = datetime.now() # izveidojam datetime objektu ar tagadējo datumu un laiku
print(f"Tagad ir {now}")

# kāds datums būs pēc 10 dienām?
from datetime import timedelta # importējam timedelta klasi, kas ļauj veikt datuma un laika aprēķinus
ten_days_later = now + timedelta(days=10) # pievienojam 10 dienas tagadējam datumam
print(f"Datums pēc 10 dienām būs {ten_days_later}")

# vēl varam izmanto rēķinot cik laiks pagājis kaut ko darot
start_time = datetime.now() # saglabājam sākuma laiku
# teiksim mēs gribam izpildīt kādu kodu, kas aizņem laiku, piemēram, izdrukāt kvadrātus no 1 līdz 1000000
result = 0
for i in range(1, 1_000_001):
    result += i ** 2
end_time = datetime.now() # saglabājam beigu laiku
# izdrukājam cik daudz laika pagājis
time_passed = end_time - start_time
print(f"Kvadrātu summa no 1 līdz 1000000 ir {result}, un tas aizņēma {time_passed} laika")

# viena no manām mīļākāja standarta bibliotēkas ir random, kas ļauj ģenerēt nejaušus skaitļus, izvēlēties nejaušas vērtības no saraksta utt.
import random
# random.seed(2026) # ja mēs gribam, lai nejaušie skaitļi būtu atkārtojami, tad varam iestatīt sēklu
random_number = random.randint(1, 100) # ģenerējam nejaušu skaitli no 1 līdz 100 ieskaitot
print(f"Nejaušs skaitlis no 1 līdz 100: {random_number}")

# man patīk ļoti ari Counter, kas ļauj saskaitīt cik reizes katra vērtība parādās sarakstā
from collections import Counter
# Counter ir dictionary ar ekstrām
my_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = Counter(my_list) # izveidojam Counter objektu no saraksta
print(f"Vērtību skaits sarakstā: {counter}")

# es varu skaitīt burtus
my_string = "Liela skaista liepa un milzīgs ozols"
letter_counter = Counter(my_string) # izveidojam Counter objektu no stringa
print(f"Burtu skaits stringā: {letter_counter}")
# top 5
print(f"Top 5 biežākie burti: {letter_counter.most_common(5)}")

# mēs varam importēt sistēmas moduļus lai uzzinātu šo to par mūsu datoru
import sys
# kāds Python
print(f"Python versija: {sys.version}")
#kāds OS
import platform
print(f"Operētājsistēma: {platform.system()} {platform.release()}")
# cik D diskā vieta
import shutil
total, used, free = shutil.disk_usage("D:/")
print(f"D diska vieta: kopā {total // (2**30)} GiB, izmantots {used // (2**30)} GiB, brīvs {free // (2**30)} GiB")