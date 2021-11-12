"""
15. Omogućite unos niza znakova te ispišite sljedeće:
	a) svaka neparna riječ (osim prve) iz niza mora biti ispisana malim znakovima po redu kako su bili unešeni
	b) svaka parna riječ (osim posljednje parne) iz niza mora biti ispisana velikim znakovima, obrnutim redom od onog kako je bila unešena
"""

a = input("Unesite znakovni niz (string): ")

words = a.split(" ")
l = len(words)
for i in range(1, l+1):
    if i % 2:
        if i == 1:
            print(words[i-1])
        else:
            print(words[i-1].lower())
    else:
        if i == l or i == l - 1:
            print(words[i-1])
        else:
            print(words[i-1].upper()[::-1])
