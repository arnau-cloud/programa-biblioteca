import os
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

def afegir_llib(db, llibre):
    if llibre == None:
        llibre = input_categor(db, True)
    position = cerc_llib(db, llibre)
    if position == None:
        print(f"S'afegirà el llibre: {llibre}")
        db.append(llibre)
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
            ans = input(f"Vols eliminar el llibre {db[posLlibre]}\n(s/n)").lower()
            if ans == "s":
                db.pop(posLlibre)
                print("Eliminat")
                break
            if ans == "n":
                print("ok, ciao")
                break
        else:
            ans = input("El llibre no existeix, vols tornar-ho a intentar?(s/n)").lower()
            if ans == "s":
                continue
            if ans == "n":
                break

def llistat_llibres(db):
    for index in range(1, len(db)):
        term_size = os.get_terminal_size()
        print('-' * term_size.columns)
        for categoria in zip(db[index].keys(), db[index].values()):
                print(categoria[0], categoria[1])

def canviar_estat(db):
    print("De quin llibre vols canviar l'estat: ")
    llibre = input_categor(db, False)
    posllib = cerc_llib(db, llibre)
    if posllib == None:
        ans = input("El llibre no existeix, vols afegir-lo?(s/n): ").lower()
        if ans == "s":
            afegir_llib(db, llibre)
    else:
        for categoria in zip(db[posllib].keys(), db[posllib].values()):
            if (categoria[0] == "Prestat: ") and (categoria[1] == True):
                ans = input(f"Vols editar el llibre {llibre} a NO prestat(s/n): ").lower()
                if ans == "s":
                    db[posllib].update({"Prestat: " : False})
            elif (categoria[0] == "Prestat: ") and (categoria[1] == False):
                ans = input(f"Vols editar el llibre {llibre} a SI prestat(s/n): ").lower()
                if ans == "s":
                    db[posllib].update({"Prestat: " : True})