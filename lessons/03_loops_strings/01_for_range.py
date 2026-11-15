"""3. nodarbība: for, range un summēšana (Python 3)."""

for number in range(1, 6):
    print("Skaitlis:", number)

print("Skaitļi ar soli 2:")
for number in range(2, 9, 2):
    print(number)

total = 0
for number in range(1, 6):
    total += number
print("Summa no 1 līdz 5:", total)  # 15

even_total = 0
for number in range(1, 11):
    if number % 2 == 0:
        even_total += number
print("Pāra skaitļu summa no 1 līdz 10:", even_total)  # 30

print("Dilstoša secība:")
for number in range(5, 0, -1):
    print(number)
