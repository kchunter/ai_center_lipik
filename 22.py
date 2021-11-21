"""
22. Napravite funkciju koja prima brojeve i vraća redom:
	a) umnožak tih brojeva
	b) zbroj tih brojeva 
	c) poredak po veličini (descending)
	d) tuple prostih brojeva koji su unešeni
	e) tuple parnih brojeva koji su unešeni
	*uzmite rezultate te funkcije te ih zapišite u file def_rez.txt

"""

#Napravit ću samo pronalazak prostih brojeva i spremanje u tekstualnu datoteku (ostalo je lagano)

def je_li_prost(n):

	prost = True
	for i in range(2, round(n**(1/2) + 1)):
		if not n % i:
			prost = False
	return True if prost and n > 1 else False

arr = [1, 2, 7, 10, 16, 18, 19]
result = filter(je_li_prost, arr)

string_ints = [str(elem) for elem in result]
str_of_ints = ",".join(string_ints)

f = open("def_rez.txt","w+")
f.write(str_of_ints)
f.close()
