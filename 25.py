"""
25. Potrebno je napraviti algoritam koji prima string liste s tri objekta. Navedeni objekti su zapravo rječnici(dictionaries) s 2 key-value para - gdje su “name” i “price” ključevi. Nazovite navedeni string json_string
#
	Primjer: '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'

	Navedeni algoritam mora riješiti sljedeće zadatke: 
		-->sortirati elemente liste po “price” ključu tako da ide od najmanje do najveće vrijednosti koja se nalazi pod “price”
		-->ukoliko su cijene dvaju proizvoda iste, onda mora sortirati ta dva proizvoda po abecedi unazad.
		-->Mora biti reproducibilan, tj. taj algoritam morate importati u drugoj skripti pod nazivom main.py 

	Testiranje: 
		'[{"name":"pivo","price":7.99},{"name":"vino","price":35.99},{"name":"rakija","price":50}]'
		'[{"name":"paprika","price":11.99},{"name":"jaja","price":11.99},{"name":"kobasice","price":18.04}]'
		'[{"name":"sir","price":35.14},{"name":"slanina","price":40.54},{"name":"rajčica","price":9.99}]'
"""
import json

def sort_by_some_rules(json_string):
    dzejson = json.loads(json_string)
    first_sort = sorted(dzejson, key=lambda x: x['price'])
    l = len(first_sort)
    for i in range(l-1): #Prvi dio sortiranja sam obavio pomoću funkcije sorted, ali ovaj drugi dio sam htio samostalno riješiti. Zasigurno nije najoptimalnije, ali mi je takav način prvi pao na pamet
        for j in range(i+1, l):
            if first_sort[i]['price'] == first_sort[j]['price']:
                if first_sort[i]['name'] < first_sort[j]['name']:
                    tmp = first_sort[i]
                    first_sort[i] = first_sort[j]
                    first_sort[j] = tmp
    return dzejson, first_sort

json_string = '[{"name":"sir","price":35.14},{"name":"slanina","price":35.14},{"name":"rajčica","price":35.14}]'#'[{"name":"kobasice","price":18.04},{"name":"jaja","price":11.99},{"name":"paprika","price":11.99}]'
prije, poslije = sort_by_some_rules(json_string)
print(f"Prije sortiranja: {prije}\n")
print(f"Nakon sortiranja: {poslije}")
