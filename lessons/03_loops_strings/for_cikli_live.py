# while cikls ir labs kad nezinam cik ilgi
# ar for ciklu mēs izpildam darbību konkretu skaitu reižu
# tehniski for cikls iet cauri kaut kādai virknei/kolekcijai
# viena šāda virkne - pusgatava ir range objekts kas atgriež skaitļus

# teiksim 5 reizes
for n in range(5): # n ir vienkārss mainīgais
    print(f"n tagad ir {n}")

print(f"Ārpus cikla n ir {n}")

# ja gribam sākt ar 1 tad definejam range(start-INCLUSIVE,stop-EXCLUDED)
for n in range(1,6): # why 6 , because range end is NOT included
    print(f"n šajā ciklā ir {n}")

# pilnā sintakse for ciklam ar range ir
# range(START, END, STEP) atkal END nav iekļauts

for number in range(100, 200+1, 20): # ja vajag iekļaut 200 tad vienkārši pieskaitam 1 :)
    print(f"number ir {number}")

# sum nevajag lietot kā mainīgo jo tā ir python funkcija
# summa ir ok
# total arī ok
summa = sum(range(1_000,10_000, 1_000))
print(f"1000 līdz 9000 pa 1000 kopa ir {summa}")
pirmie_100 = sum(range(101))
print(f"Pirmie 100 skaitļi no 0 līdz 100 ieskaitot summa ir {pirmie_100}")

# for tātad iet cauri jebkādām virknēm
# vai mēs zinam vēl kādu virkni?

# teksts savā būtība ir virkne ar simboliem
# tehniski Python teksts ir virkne ar 1 teksta vienībam , jo Python neizmanot simbola tieši

name = "Valdis"
for burts in name:
    print(f"Apstrādājam burtu {burts}")