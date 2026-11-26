# es varu lietot pakotni, kas satur vairākus moduļus
# importējot pakotni, mēs varam piekļūt visiem moduļiem
# tipiski ir āri pārsaukt moduļus, lai tie būtu vieglāk lietojami
import my_pakotne.apaksmodulis_a as a_modulis
import my_pakotne.apaksmodulis_b as b_modulis   

print(f"Vārds ar lielajiem burtiem: {a_modulis.yell_name('Alice')}")
print(f"Reizināts ar 100: {a_modulis.multiply_by_100(5)}")
print(f"4. pakāpe: {b_modulis.power_of_4(2)}")