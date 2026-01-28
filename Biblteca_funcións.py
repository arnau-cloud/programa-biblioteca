import os
#Funció per a afegir llibres
def input_categor(db, demanarPrestat: bool):
    dades = dict()
    for categoria in zip(db[0].keys(), db[0].values()):
        while True:
            try:
                if (demanarPrestat == False) and (categoria[0] == "Prestat"):
                    break
                else:
                    match categoria[1]:
                        case bool():
                            ans = input(f"Introdueix la dada {categoria[0]} (s/n): ")
                            if ans == "s":
                                dades.update({categoria[0] : True})
                            elif ans == "n":
                                dades.update({categoria[0] : False})
                            else:
                                raise ValueError
                        case int():
                            dades.update({categoria[0] : int(input(f"Introdueix la dada {categoria[0]}: "))})
                        case str():
                            dades.update({categoria[0] : (input(f"Introdueix la dada {categoria[0]}: ").lower())})
                    break
            except ValueError:
                pedro_sanchez = str()
                match categoria[1]:
                    case bool():
                        pedro_sanchez = "s o n (si/no)"
                    case int():
                        pedro_sanchez = "un nombre"
                    case str():
                        pedro_sanchez = "un text"
                print(f"incompatible, la dada ha de ser {pedro_sanchez}")
    return dades

def cerc_llib(db, parametres):
    coincidències = int(); index = int()
    for index in range(1, len(db)):
        if coincidències < 2:
            for categoria in zip(db[index].keys(), db[index].values()):
                        if categoria[0] != 'Prestat':
                            for categoria2 in zip(parametres.keys(), parametres.values()):
                                if categoria == categoria2:
                                    coincidències += 1
                                    break
                        else:
                            break
        else:
            break
    if coincidències > 2: return index - 1

def afegir_llib(db, llibre = None):
    if llibre == None:
        llibre = input_categor(db, True)
    position = cerc_llib(db, llibre)
    if position == None:
        print(f"S'afegirà el llibre: {llibre}")
        db.append(llibre)
    else:
        print(f"Ja existeix el llibre: {db[position]}, \nno s'afegirà")

def elim_llibre(db):
    cont = True;
    while cont == True:
        print("Quin llibre vols eliminar?: ")
        llibre = input_categor(db, False)
        posLlibre = cerc_llib(db, llibre)
        if posLlibre != None:
            while True:
                ans = input(f"Vols eliminar el llibre {db[posLlibre]}\n(s/n): ").lower()
                if ans == "s":
                    db.pop(posLlibre)
                    print("Eliminat")
                    cont = False
                    break
                if ans == "n":
                    print("ok, ciao")
                    cont = False
                    break
                else:
                    print("Incompatible, ha de ser s o n (si/no)")
                    continue
        else:
            while True:
                ans = input("El llibre no existeix, vols tornar a intentar-ho?(s/n): ").lower()
                if ans == "s":
                    break
                if ans == "n":
                    cont = False
                    break
                else:
                    print("Incompatible, ha de ser s o n (si/no)")
                    continue

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
            if (categoria[0] == "Prestat") and (categoria[1] == True):
                ans = input(f"Vols editar el llibre {llibre} a NO prestat(s/n): ").lower()
                if ans == "s" or "":
                    db[posllib].update({"Prestat: " : False})
            elif (categoria[0] == "Prestat") and (categoria[1] == False):
                ans = input(f"Vols editar el llibre {llibre} a SI prestat(s/n): ").lower()
                if ans == "s" or "":
                    db[posllib].update({"Prestat: " : True})

def llistar_autors(db):
    llistat = list()
    for index in range(1, len(db)):
        for categoria in zip(db[index].keys(), db[index].values()):
            if categoria[0] == "Autor" and (not(categoria[1] in llistat)):
                llistat.append(categoria[1])
    for a in llistat:
        print(a)