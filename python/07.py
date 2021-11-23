"""
7. Ispiši vrijednost broja Pi na 4 decimalna mjesta, 
kvadriraj taj broj te ga podijeli s racionalnim brojem odabranim od strane korisnika (input funkcija) i ispiši rezultat.
"""

import math

PI = math.pi
PI = round(PI, 4)
print(f"Ludolfov broj zaokružen na četiri (4) decimale: {PI}")
PI**=2
a = float(input("Unesite realni broj: "))
novi = PI / a
print(f"Novi broj: {novi}")

