"""
Hozz létre egy listát számokkal: [5, 8, 12, 15, 22].
Határozd meg a lista hosszát egy ciklus segítségével 
(a len() függvény megoldásán kívül használj for ciklusos megoldást is),
és írd ki!
"""

szamok = [5, 8, 12, 15, 22]

print(f"A lista hossza len függvénnyel {len(szamok)}")

darab = 0
for szam in szamok:
    darab += 1

print(f"A list hossza for ciklussal {darab}")