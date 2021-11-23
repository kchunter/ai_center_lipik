"""
18. Dobivate tuple sljedeće strukture: t = ("Jaje", [10, 20, 30], (5, 50, 500))
Napišite funkciju koja će printati vrijednost 20 iz tog tuplea. 
"""

t = ("Jaje", [10, 20, 30], (5, 50, 500))

def vrati_broj_20(tup):

    return tup[1][1] #Može se također printati odmah iz funkcije, ali mi je ovako bolje

rez = vrati_broj_20(t)
print(rez)