"""
10. Napišite algoritam koji uzima broj nasumične dužine te ispisuje:
a) svaku drugu znamenku s tri decimalna mjesta (0,000) 
b) zaokružen zbroj svih upravo ispisanih znamenki
"""

a = input("Unesite broj: ")
new_num = ""
for i in range(0, len(a), 2):
    print("{:.3f}".format(float(a[i])))
    new_num += a[i]

print(int(new_num))