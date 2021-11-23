"""
23. Napiši funkciju koja će za neki input broj vratiti nested listu s dužinama sub-lista koje se povećavaju za 1.
	Rezultat bi trebao izgledati ovako: 
		pyramid(0) => [ ]
		pyramid(1) => [ [1] ]
		pyramid(2) => [ [1], [1, 1] ]
		pyramid(3) => [ [1], [1, 1], [1, 1, 1] ]
		pyramid(4) => ...
"""

n = int(input("Unesite n (prirodan broj): "))

for i in range(0, n + 1):
    arr = []
    for j in range(0, i):
        arr.append((j+1)*[1])
    print(f"pyramid({i}) => {arr}")