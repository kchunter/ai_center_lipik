"""
9. Napišite algoritam koji prima nasumičan pozitivni broj manji od 86400 te pretvara taj broj iz sekunda i ispisuje koliko je to točno vrijeme u satima, minutama i sekundama
"""

import random

a = random.randint(0, 86399)
print(f"Nasumičnim izborom dobiven je broj {a}")

minute, sekunde = divmod(a, 60)
sati, minute = divmod(minute, 60)

print(f"{a} sekundi je {sati} sati, {minute} minuta i {sekunde} sekunde")


