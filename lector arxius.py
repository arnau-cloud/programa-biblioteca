with open("Arxius/biblioteca.txt", "r", encoding="utf-8") as fitxer:
    for f in fitxer:
        print(f.strip())
linia = "El Quixot,l Cervants, 6733"
dades = linia.split(",")
titol = dades[0].strip()
autor = dades[1].strip()
any = int(dades[2].strip())
print(linia)
print(dades)
print(titol)
print(autor)
print(any)