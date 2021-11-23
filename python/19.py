"""
19. Omogućite unos dviju vrijednosti u dva navrata korisniku.
Svaki par vrijednosti zapišite u jedan tuple.
Zamijenite vrijednosti ovih dvaju tupleova te ispišite rezultat. 
"""

for i in range(2):

    a = input("Unesite prvu vrijednost: ")
    b = input("Unesite drugu vrijednost: ")
    locals()["tup" + str(i+1)] = (a, b)

print(f"Prije promjene\ntup1 = {tup1}, tup2 = {tup2}")

tup1, tup2 = tup2, tup1

print(f"Nakon promjene\ntup1 = {tup1}, tup2 = {tup2}")