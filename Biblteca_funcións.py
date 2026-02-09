import os
term_size = os.get_terminal_size()  # Espai a la terminal per a imprimir linies


def input_categor(db, demanarPrest=False):

    """Afegeix un nou llibre

    db --> Base de dades que editar

    demanarPrest --> Condiciona si fer un input
                     on es demani si està prestat
    """
    dades = dict()
    for categoria in zip(db[0].keys(), db[0].values()):
        while True: #bucle
            try:
                # Si demanarPrestat es fals ignora l'apartat "Prestat"
                if (demanarPrest is False) and (categoria[0] == "Prestat"):
                    break
                else:
                    # Demanant inputs en base al tipus de dada
                    match categoria[1]:
                        case bool():
                            ans = input(f"\t╚{"═"*5}> Introdueix si està {categoria[0]} (s/n): ").lower().strip()
                            if ans == "s":
                                dades.update({categoria[0]: True})
                            elif ans == "n":
                                dades.update({categoria[0]: False})
                            else:
                                raise ValueError
                        case int():
                            dades.update({categoria[0]: int(input(f"\t╚{"═"*5}> Introdueix la dada {categoria[0]}: ").strip())})
                        case str():
                            dades.update({categoria[0]: (input(f"\t╚{"═"*5}> Introdueix la dada {categoria[0]}: ").lower().strip())})
                    break
            except ValueError:
                pedro_sanchez = str()
                # Indica la mena dada si hi ha un error
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
    """Cerca un llibre

    db --> Base de dades que editar

    parametres --> Quin llibres s'ha de buscar
    """
    index = int()
    for index, categoria in enumerate(db, 1):
        llistat = categoria.copy()
        llistat.pop("Prestat")
        if llistat == parametres:
            return index - 1
            break


def afegir_llib(db, llibre=None):
    if llibre is None:
        print('-' * term_size.columns)
        print("\n\tQuin llibre vols afegir: ")
        llibre = input_categor(db, True)
    position = cerc_llib(db, llibre)
    if position is None:
        print("\tS'afegirà el llibre: ", end="")
        llistat_llibres(db, llibre)
        db.append(llibre)
    else:
        print(f"Ja existeix el llibre: {db[position]}, \nno s'afegirà")


def elim_llibre(db):
    cont = True
    while cont is True:
        print("Quin llibre vols eliminar?: ")
        llibre = input_categor(db)
        posLlibre = cerc_llib(db, llibre)
        if posLlibre is not None:
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


def canviar_estat(db):
    print("De quin llibre vols canviar l'estat")
    llibre = input_categor(db)
    posllib = cerc_llib(db, llibre)
    if posllib is None:
        while True:
            print("El llibre no existeix, ", end="")
            afegir_llib(db, llibre)
    else:
        if db[posllib]["Prestat"] is True:
            while True:
                print("Vols editar el llibre ", end="")
                llistat_llibres(db, db[posllib])
                ans = input(f"a NO prestat(s/n): ").lower().strip()
                if ans == "s" or "":
                    db[posllib].update({"Prestat": False})
                    break
                elif ans == "n":
                    break
                else:
                    print("Incompatible, ha de ser s o n (si/no)")
        elif db[posllib]["Prestat"] is False:
            while True:
                ans = input(f"Vols editar el llibre {llibre} a SI prestat(s/n): ").lower().strip()
                if ans == "s" or "":
                    db[posllib].update({"Prestat": True})
                    break
                elif ans == "n":
                    break
                else:
                    print("Incompatible, ha de ser s o n (si/no)")


def llistat_llibres(db, specific=None):
    if specific is None:
        print('-' * term_size.columns)
        for index in range(1, len(db)):
            for categoria in zip(db[index].keys(), db[index].values()):
                    print(f"            {categoria[0]}: {categoria[1]}")
            print('-' * term_size.columns)
    else:
        for categoria in zip(specific.keys(), specific.values()):
                print(f"{categoria[0]}: {categoria[1]}", end=", ")


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
