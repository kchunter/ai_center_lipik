"""
16. Unesite dva proizvoljna niza znakova te ih spremite u dvije varijable. 
Prvi niz znakova mora imati više unesenih riječi od drugog niza znakova.
Od vrijednosti te dvije varijable napravite dvije liste te kreirajte konačni rječnik 
gdje će vrijednosti iz druge liste biti ključevi, a vrijednosti iz prve liste postati vrijednosti koje se pozivom ključa ispisuju.
"""

while 1:
    a = input("Unesite prvi znakovni niz (string): ")
    b = input("Unesite drugi znakovni niz (string): ")
    print()
    words_a = a.split(" ") #Pretpostavka da je niz takav da su sve riječi odvojene samo s razmakom
    words_b = b.split(" ")
    words_a_len = len(words_a)
    words_b_len = len(words_b)
    
    if words_a_len > words_b_len:
        break

#One of the options
zipped = zip(words_a, words_b)
dic = dict(zipped)
print(dic)
