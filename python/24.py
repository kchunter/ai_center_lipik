"""
24. Automat s čokoladicama prima bilo koji iznos u kunama i vraća kovanice u sljedećim oblicima:
	1 lipa
	2 lipe
	5 lipa
	10 lipa
	20 lipa
	50 lipa
	1 kuna
	2 kune
	5 kuna
Potrebno je napisati funkciju koju će koristiti navedeni automat s čokoladicama kako bi vratio ostatak novca korisniku. 
Pretpostavka je da automat uvijek vraća najmanji mogući broj kovanica.
Funkcija prima 2 parametra - količinu novca kojeg je korisnik ubacio i cijenu proizvoda
Funkcija vraća listu brojeva. Svaki od tih brojeva predstavlja količinu jedne vrste kovanice.

Primjer: getChange(20, 3.99) -> [1, 0, 0, 0, 0, 0, 1, 0, 3]  ((1lp, 2lp, 5lp, 10lp, 20lp, 50lp, 1kn, 2kn, 5kn))

Testiranje:
get_change(3.14, 1.99) -> [0, 0, 1, 1, 0, 0, 1, 0, 0] 
get_change(4, 3.14) -> [1, 0, 0, 0, 0, 0, 1, 0, 3] 
get_change(0.45, 0.34) -> [1, 0, 0, 0, 0, 0, 1, 0, 3] 
"""
import math

def get_change(ukupni_novac, cijena_proizvoda): #Ovdje mi također nije bio cilj riješiti na najoptimalniji način pa sam riješio 
                                                #na način koji mi je prvi pao na pamet, bez pretraživanja boljih rješenja na internetu

    kovanice = ((500, '5kn'), (200, '2kn'), (100, '1kn'), (50, '50lp'), (20, '20lp'), (10, '10lp'), (5, '5lp'), (2, '2lp'), (1, '1lp'))
    if ukupni_novac < cijena_proizvoda:
        print("Nedovoljan iznos!")
        return  
    ostatak = round(float(ukupni_novac - cijena_proizvoda), 2)
    decim, cijeli = math.modf(ostatak)
    lipe = int(cijeli) * 100
    lipe_ostalo = round(decim*100)
    lipe+=lipe_ostalo
    arr = []
    for i in range(len(kovanice)):
        cijelih, ostatak = divmod(lipe, kovanice[i][0])
        lipe = ostatak
        arr.append((cijelih, kovanice[i][1]))
    return arr

result = get_change(500, 4)
print(result)


