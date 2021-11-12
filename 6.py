"""
6. Unesi jedan nasumični broj. 
Ispiši aritmetičku sredinu onoliko brojeva(0-101) koliko je iznosio uneseni nasumični broj.
Navedeni broj uzmi kao vrijednost opsega kruga te ispiši vrijednost polumjera navedenog kruga.
"""
import math

a = int(input("Unesite slučajan broj: "))

if a > 101:
    zbroj = 101*(101+1)/2
    a_s = zbroj / 102
    opseg_kr = a_s
    print(f"Radijus kruga s opsegom {a_s} iznosi {opseg_kr / (2*math.pi)}")
elif a < 0:
    print(f"Radijus kruga s opsegom {0} iznosi {0}")
else:
    zbroj = a*(a+1)/2
    a_s = zbroj / (a+1)
    opseg_kr = a_s
    print(f"Radijus kruga s opsegom {a_s} iznosi {opseg_kr / (2*math.pi)}")