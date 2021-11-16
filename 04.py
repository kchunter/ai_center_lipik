"""
4. Napišite program koji će u varijable a i b spremiti dva dvoznamenkasta broja. 
U varijablu a pohranite zadnju znamenku broja koji se nalazi u varijabli b, 
a u varijablu b pohranite zadnju znamenku broja koja se nalazi u varijabli a. 
Ispišite sadržaj varijabli a i b.
"""

#First option
#while 1:
#    a = input("Unesite prvi dvoznamenkasti broj: ")
#    b = input("Unesite drugi dvoznamenkasti broj: ")
#    len_a = len(a)
#    len_b = len(b)

#    if len_a == 2 and len_b == 2 and any(map(str.isdigit, a+b)):
#        break
#    print()

#last_a = a[-1]
#a = int(b[-1])
#b = int(last_a)

#print(f"prvi = {a}, drugi = {b}")



#Second option
a = int(input("Unesite prvi dvoznamenkasti broj: "))
b = int(input("Unesite drugi dvoznamenkasti broj: "))

tmp = a
a = b % 10
b = tmp % 10

print(f"prvi = {a}, drugi = {b}")

