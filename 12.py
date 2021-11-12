"""
12. Nađite sva ponavljanja ‘stol’ u zadanom stringu zanemarujući velika i mala slova: „U kuhinji je stol. STOL je novi.”
"""

a = "U kuhinji je stol. STOL je novi."

b = a.lower()
idx = 0
counter = 0
while 1:
    l = len("stol")
    idx = b.find("stol", idx)
    if idx == -1:
        break
    print(a[idx:idx+l])
    idx+=1
    counter+=1

print(f"Riječ 'stol' javlja se {counter} puta u oblicima koju su prikazan iznad")