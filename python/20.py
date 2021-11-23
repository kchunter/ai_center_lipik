"""
20. Omogućite korisniku unos dviju vrijednosti n puta korisniku. 
Sortirajte sve unose koristeći druge vrijednosti iz svakog unosa.
"""

n = int(input("Unesite n: "))
arr = list()
for i in range(n):
    a = int(input("Unesite prvi broj: ")) #Ograničeno na cijele brojeve
    b = int(input("Unesite drugi broj: "))
    print()
    arr.append([a, b])

print(f"Lista prije sortiranja {arr}")
rez = sorted(arr, key=lambda x: x[1])
print(f"Lista nakon sortiranja {rez}")