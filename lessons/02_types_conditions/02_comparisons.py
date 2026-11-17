"""2. nodarbība: salīdzināšanas operatori un robežvērtības."""
x = 12
print("x:", x)
print("x == 12:", x == 12)  # Vienādība (nevis piesaiste ar =).
print("x != 10:", x != 10)
print("x > 12:", x > 12)
print("x >= 12:", x >= 12)
print("x < 20:", x < 20)
print("x <= 10:", x <= 10)
print("Salīdzinājuma tips:", type(x >= 12))

# Python atbalsta salīdzinājumu ķēdes.
vecums = 18
print("18 <= vecums < 65:", 18 <= vecums < 65)
print("0 <= vecums <= 120:", 0 <= vecums <= 120)

# Viena simbola izmaiņa var mainīt rezultātu tieši uz robežas.
punkti = 60
print("punkti > 60:", punkti > 60)
print("punkti >= 60:", punkti >= 60)

# Negatīvs vecums nav derīgs, lai gan tas ir int.
vecums = -1
print("Vai vecums ir derīgs?", 0 <= vecums <= 120)
