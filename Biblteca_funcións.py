import os
term_size = os.get_terminal_size()
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
                            ans = input(f"\t╚{"═"*5}> Introdueix si està {categoria[0]} (s/n): ")
                            if ans == "s":
                                dades.update({categoria[0] : True})
                            elif ans == "n":
                                dades.update({categoria[0] : False})
                            else:
                                raise ValueError
                        case int():
                            dades.update({categoria[0] : int(input(f"\t╚{"═"*5}> Introdueix la dada {categoria[0]}: "))})
                        case str():
                            dades.update({categoria[0] : (input(f"\t╚{"═"*5}> Introdueix la dada {categoria[0]}: ").lower().strip())})
                    break
            except ValueError:
                pedro_sanchez = str()
                match categoria[1]:
                    case bool():
                        pedro_sanchez = "s o n (si/no)"
                    case int():
                        pedro_sanchez = "un nombre (0-9)"
                    case str():
                        pedro_sanchez = "un text"
                print(f"\tincompatible, la dada ha de ser {pedro_sanchez}")
    return dades

def cerc_llib(db, parametres):
    index = int()
    for index, categoria in enumerate(db, 1):
        llistat = categoria.copy()
        llistat.pop("Prestat")
        if llistat == parametres:
            return index - 1
            break

def afegir_llib(db, llibre = None):
    if llibre == None:
        print('-' * term_size.columns)
        print("\n\tQuin llibre vols afegir: ")
        llibre = input_categor(db, True)
    position = cerc_llib(db, llibre)
    if position == None:
        print("\tS'afegirà el llibre: ", end= "")
        llistat_llibres(db, llibre)
        db.append(llibre)
    else:
        print(f"Ja existeix el llibre: {db[position]}, \nno s'afegirà")

def elim_llibre(db):
    cont = True
    while cont == True:
        print("Quin llibre vols eliminar?: ")
        llibre = input_categor(db, False)
        posLlibre = cerc_llib(db, llibre)
        if posLlibre != None:
            while True:
                print("Vols eliminar el llibre ", end="")
                llistat_llibres(db, db[posLlibre])
                ans = input("(s/n): ").lower().strip()
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
                ans = input("El llibre no existeix, vols tornar a intentar-ho?(s/n): ").lower().strip()
                if ans == "s":
                    break
                if ans == "n":
                    cont = False
                    break
                else:
                    print("Incompatible, ha de ser s o n (si/no)")
                    continue

def llistat_llibres(db, specific = None):
    if specific == None:
        print('-' * term_size.columns)
        for index in range(1, len(db)):
            for categoria in zip(db[index].keys(), db[index].values()):
                    print(f"            {categoria[0]}: {categoria[1]}")
            print('-' * term_size.columns)
    else:
        for categoria in zip(specific.keys(), specific.values()):
                print(f"{categoria[0]}: {categoria[1]}", end = ", ")

def canviar_estat(db):
    print("De quin llibre vols canviar l'estat")
    llibre = input_categor(db, False)
    posllib = cerc_llib(db, llibre)
    if posllib == None:
        while True:
            print("El llibre no existeix, ", end = "")
            afegir_llib(db, llibre)   
    else:
        if db[posllib]["Prestat"] == True:
            while True:
                print("Vols editar el llibre ", end = "")
                llistat_llibres(db, db[posllib])
                ans = input(f"a NO prestat(s/n): ").lower().strip()
                if ans == "s" or "":
                    db[posllib].update({"Prestat" : False})
                    break
                elif ans == "n":
                    break
                else:
                    print("Incompatible, ha de ser s o n (si/no)")
        elif db[posllib]["Prestat"] == False:
            while True:
                ans = input(f"Vols editar el llibre {llibre} a SI prestat(s/n): ").lower().strip()
                if ans == "s" or "":
                    db[posllib].update({"Prestat" : True})
                elif ans == "n":
                    break
                else:
                    print("Incompatible, ha de ser s o n (si/no)")

def llistar_autors(db):
    llistat = set()
    for index in range(1, len(db)):
        for categoria in zip(db[index].keys(), db[index].values()):
            if categoria[0] == "Autor":
                llistat.add(categoria[1])
    print('-' * term_size.columns)
    for a in llistat:
        print(f"            {a}")
        print('-' * term_size.columns)