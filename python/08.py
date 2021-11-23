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

import random

def median(arr):
    l = len(arr)
    arr.sort()
    if l % 2:
        return arr[l//2]
    return (arr[l//2] + arr[l//2-1]) / 2

def mode(arr):
    dic = {}
    for elem in arr:
        if elem in dic:
            dic[elem] += 1
        else:
            dic[elem] = 1
    if all(map(lambda x: x == 1, dic.values())):
        return
    else:
        return list(filter(lambda x: dic[x] == max(dic.values()), dic.keys()))

def average(arr):
    sum = 0
    count = 0
    for elem in arr:
        sum+=elem
        count+=1
    return sum / count

a = int(input("Unesite broj: "))
new_list = [random.randint(0, 1001) for i in range(a)]
mod = mode(new_list)
if type(mod) == list and len(mod) == 1:
    mod = mod[0]
print(f"Početna lista: {new_list}")
print(f"Medijan: {median(new_list)}")
print(f"Mod: {mod}")
print(f"Aritmetička sredina: {average(new_list)}")

