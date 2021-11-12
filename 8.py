"""
8 Unesi neki nasumični broj kojeg ćeš uzeti kao vrijednost duljine liste u koju se trebaju spremiti vrijednosti od 0 do 1001. 
	Ispiši sljedeće vrijednosti na ekran:
		a) medijan
		b) mod
		c) aritmetičku vrijednost
		d) sve brojeve koji se u definiranoj listi nalaze ispred vrijednosti koju smo izračunali kao medijan navedene liste
		e) sve brojeve koji su manji od vrijednosti koju smo izračunali kao medijan navedene liste 

	*Bonus: Napravite novu listu koja sadrži samo vrijednosti koje su za 10% veće ili manje od aritmetičke sredine
"""

def median(arr):
    l = len(arr)
    med = (arr[l//2] + arr[l//2-1]) / 2
    if l % 2:
        med = arr[l//2]
    return med

def mode(arr):
    dic = {}
    for elem in arr:
        if elem in dic:
            dic[elem] += 1
        else:
            dic[elem] = 1
    mod = max(dic, key=dic.get)
    return mod

def average(arr):
    sum = 0
    count = 0
    for elem in arr:
        sum+=elem
        count+=1
    return sum / count

a = int(input("Unesite broj: "))

if a > 1001:
    new_list = [i for i in range(1001)]
elif a <= 0:
    raise Exception("Invalid number. The number must be greater than 0")
else:
    new_list = [i for i in range(a)]
    med = median(new_list)
    mod = mode(new_list)
    avg = average(new_list)

