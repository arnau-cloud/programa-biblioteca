import os
term_size = os.get_terminal_size()  # Espai a la terminal per imprimir linies


def input_categor(db, demanarPrest=False):
    """
    Demana a l'usuari les dades d'un llibre segons la plantilla db[0].

    Parametres:
      db --> llista de dicts amb db[0] = plantilla de camps i tipus.
      demanarPrest --> Si és False, no es demana l'estat de préstec.

    Retorna:
      Un dict amb les dades introduïdes.
    """

    dades = dict()
    for categoria in zip(db[0].keys(), db[0].values()):
        while True:  # Bucle fins que les categories siguin correctes
            try:
                # Si demanarPrestat es fals ignora l'apartat "Prestat"
                if (demanarPrest is False) and (categoria[0] == "Prestat"):
                    break
                else:
                    # Demanant inputs en base al tipus de dada
                    match categoria[1]:
                        case bool():
                            ans = input(
                                f"\t╚{"═"*5}> Introdueix si està "
                                f"{categoria[0]} (s/n): "
                            ).lower().strip()
                            if ans == "s":
                                dades.update({categoria[0]: True})
                            elif ans == "n":
                                dades.update({categoria[0]: False})
                            else:
                                raise ValueError
                        case int():
                            ans = int(input(
                                        f"\t╚{'═'*5}> Introdueix la dada "
                                        f"{categoria[0]}: "
                                    ).strip())
                            dades.update({categoria[0]: ans})
                        case str():
                            ans = input(
                                    f"\t╚{"═"*5}> Introdueix la dada "
                                    f"{categoria[0]}: "
                                ).lower().strip()
                            dades.update({categoria[0]: ans})
                    break
            except ValueError:
                pedro_sanchez = str()
                # Indica la mena de dada si hi ha un error
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
    """
    Cerca un llibre amb la plantilla db[0] i els paràmetres donats.

    Parametres:
    db --> Base de dades que iterar.
    parametres --> Quin llibres s'ha de buscar.

    Retorna:
    La posició del llibre a la base de dades o None si no existeix.
    """
    index = int()
    for index, categoria in enumerate(db, 1):
        llistat = categoria.copy()
        llistat.pop("Prestat")
        if llistat == parametres:
            return index - 1
            break


def afegir_llib(db, llibre=None):
    """
    Afegeix un llibre a la base de dades si no existeix.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
      llibre --> diccionari amb les dades del llibre o omitir.
    """
    if llibre is None:
        print('-' * term_size.columns)
        print("\n\tQuin llibre vols afegir: ")
        llibre = input_categor(db, True)
        
    position = cerc_llib(db, llibre)
    if position is None:
        print("\tS'ha afegit el llibre: ", end="")
        llistat_llibres(db, llibre)
        db.append(llibre)
    else:
        print(f"Ja existeix el llibre: {db[position]}, \nno s'afegirà")


def elim_llibre(db):
    """
    Elimina un llibre de la base de dades.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
    """
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
    """
    Canvia l'estat 'Prestat' d'un llibre existent o afegeix-lo si no existeix.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
    """
    print('-' * term_size.columns)
    print("\nDe quin llibre vols canviar l'estat")
    llibre = input_categor(db)
    posllib = cerc_llib(db, llibre)
    if posllib is None: # Si el llibre no existeix, es demana si es vol afegir
        while True:
            ans = input("El llibre no existeix, vols afegir-lo?(s/n): ").lower()
            if ans == "s":
                llibre.update({"Prestat": False})
                afegir_llib(db, llibre)
                break
            elif ans == "n":
                break
            else:
                print("Incompatible, ha de ser s o n (si/no)")
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
    """
    Imprimeix llibres per pantalla.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
      specific --> dict amb una entrada específica o None per llistar tots.
    """
    if specific is None: # Imprimeix un llibre espcífic si existeix
        print('-' * term_size.columns)
        # Itera pel llibre específic i imprimeix les seves categories
        for index in range(1, len(db)):
            for categoria in zip(db[index].keys(), db[index].values()):
                    print(f"\t\t\t{categoria[0]}: {categoria[1]}")
            print('-' * term_size.columns)
    else:
        # Imprimeix tots els llibres amb format
        for categoria in zip(specific.keys(), specific.values()):
                print(f"{categoria[0]}: {categoria[1]}", end=", ")


def llistar_autors(db):
    """
    Mostra la llista d'autors únics de la base de dades.

    Parametres:
        db --> llista de dicts (db[0] és la plantilla).
    """
    llistat = set()
    # Itera sobre la base de dades i afegeix els autors al conjunt
    for index in range(1, len(db)):
        for categoria in zip(db[index].keys(), db[index].values()):
            if categoria[0] == "Autor":
                llistat.add(categoria[1])
    
    print('-' * term_size.columns)
    for a in llistat: # Imprimeix amb format
        print(f"\t\t\t{a}")
        print('-' * term_size.columns)
