"""
17. Unesite tri proizvoljna niza znakova te ih spremite u tri varijable. 
Ispišite na ekran znakove (characters) koji su zajednički svim unesenim vrijednostima
"""

a = input("Unesite prvi znakovni niz (string): ")
b = input("Unesite drugi znakovni niz (string): ")
c = input("Unesite treci znakovni niz (string): ")

skup_a, skup_b, skup_c = set(a), set(b), set(c)
presjek = skup_a & skup_b & skup_c
print(presjek)