#Funció per a afegir llibres
def input_categor(db, demanarPrestat: bool):
    dades = dict()
    for categoria in zip(db[0].keys(), db[0].values()):
        while True:
            try:
                if (demanarPrestat == False) and (categoria[0] == "Prestat: "):
                    break
                else:
                    match categoria[1]:
                        case bool():
                            dades.update({categoria[0] : bool(input(f"Introdueix la dada {categoria[0]}"))})
                        case int():
                            dades.update({categoria[0] : int(input(f"Introdueix la dada {categoria[0]}"))})
                        case str():
                            dades.update({categoria[0] : (input(f"Introdueix la dada {categoria[0]}").lower())})
                    break
            except ValueError:
                pedro_sanchez = str()
                match categoria[1]:
                    case bool():
                        pedro_sanchez = "un bolea(True/False)"
                    case int():
                        pedro_sanchez = "un nombre"
                    case str():
                        pedro_sanchez = "un text"
                print(f"incompatible, la dada ha de ser {pedro_sanchez}")
    return dades

def cerc_llib(db, parametres):
    coincidències = int(); index1 = int()
    for index1 in range(1, len(db)):
        if coincidències < 2:
            for categoria in zip(db[index1].keys(), db[index1].values()):
                        if categoria[0] != 'Prestat: ':
                            for categoria2 in zip(parametres.keys(), parametres.values()):
                                if categoria == categoria2:
                                    coincidències += 1
                                    break
                        else:
                            break
        else:
            break
    if coincidències > 2: return index1

def afegir_llib(db):
    llibre = input_categor(db, True)
    position = cerc_llib(db, llibre)
    if position == None:
        print(f"S'afegirà el llibre: {llibre}")
    else:
        print(f"Ja existeix el llibre: {db[position]}, \nno s'afegirà")

#    coincidencies = 0
#    for entrades in db:
#        if not(llibre == entrades):
#            db.append(llibre)
#            break
#        else:
#            coincidencies += 1
#            break
#    if coincidencies != 0:
#        if input(f"Hi ha una entrada en la que coincideixen {coincidencies} paràmetres, vols afegir el llibre igualment? (s/n): ") == "s":
#            db.append(llibre)

def elim_llibre(db):
    while True:
        print("Quin llibre vols eliminar?: ")
        llibre = input_categor(db, False)
        posLlibre = cerc_llib(db, llibre)
        if posLlibre != None:
            res = input(f"Vols eliminar el llibre {db[posLlibre]}\n(S/N)").lower()
            if res == "s":
                db.pop(posLlibre)
                print("Eliminat")
                break
            if res == "n":
                print("ok, ciao")
                break
        else:
            res = input("El llibre no existeix, vols tornar-ho a intentar?(S/N)").lower()
            if res == "s":
                continue
            if res == "n":
                break

def llistat_llibres(db):
    for index in range(1, len(db)):
        for categoria in zip(db[index].keys(), db[index].values()):
            for index2 in range(0, len(categoria)):
                print(categoria)