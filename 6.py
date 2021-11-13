"""
6. Unesi jedan nasumični broj. 
Ispiši aritmetičku sredinu onoliko brojeva(0-101) koliko je iznosio uneseni nasumični broj.
Navedeni broj uzmi kao vrijednost opsega kruga te ispiši vrijednost polumjera navedenog kruga.
"""
import math, random, statistics

a = int(input("Unesite prirodan broj: ")) 
arr = [random.randint(0, 101) for i in range(a)]
avg = statistics.mean(arr)
print("Prosjek: ", avg)
print(f"Radijus kruga s opsegom {avg} iznosi {round(avg / (2*math.pi), 2)}")