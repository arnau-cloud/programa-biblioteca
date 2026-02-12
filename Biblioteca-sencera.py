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
    # Iterem sobre les categories de la plantilla
    for categoria in zip(db[0].keys(), db[0].values()):
        while True:  # Bucle fins que les categories siguin correctes
            try:
                # Si demanarPrestat es fals ignora l'apartat "Prestat"
                if (demanarPrest is False) and (categoria[0] == "Prestat"):
                    break
                else:
                    # Demanem inputs en base al tipus de dada i ho afegim
                    match categoria[1]:
                        case bool():
                            # Esperem 's' o 'n'; normalitzem entrada
                            # Ho afegim amb la categoria i el valor introduït
                            ans = input(
                                f"\t╚{"═"*5}> Introdueix si està "
                                f"{categoria[0]} (s/n): "
                            ).lower().strip()
                            if ans == "s":
                                dades.update({categoria[0]: True})
                            elif ans == "n":
                                dades.update({categoria[0]: False})
                            else:
                                # Forcem reintentar per entrada invàlida.
                                raise ValueError
                        case int():
                            ans = int(input(
                                f"\t╚{'═'*5}> Introdueix la dada "
                                f"{categoria[0]}: "
                            ).strip())
                            # Ho afegim amb la categoria i el valor introduït
                            dades.update({categoria[0]: ans})
                        case str():
                            ans = input(
                                f"\t╚{"═"*5}> Introdueix la dada "
                                f"{categoria[0]}: "
                            ).lower().strip()
                            if ans == "":  # Forcem reintentar per entrada en blanc.
                                raise ValueError
                            # Ho afegim amb la categoria i el valor introduït
                            dades.update({categoria[0]: ans})
                    break
            except ValueError:
                # Indica la mena de dada que s'espera si hi ha un error
                pedro_sanchez = str()
                match categoria[1]:
                    case bool():
                        pedro_sanchez = "s o n (si/no)"
                    case int():
                        pedro_sanchez = "un nombre (0-9)"
                    case str():
                        pedro_sanchez = "un text"
                print(f"\t\tincompatible, la dada ha de ser {pedro_sanchez}")
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
    # Iterem sobre la base de dades i extraiem el index, que després retornem
    for index, categoria in enumerate(db, 1):
        llistat = categoria.copy()
        llistat2 = parametres.copy()
        # No tenim en compte el camp "Prestat", s'elimina
        llistat.pop("Prestat")
        if "Prestat" in llistat2:
            llistat2.pop("Prestat")
        if llistat == llistat2:
            return index - 1 # Retornem al posició i compensem la plantilla
            break


def afegir_llib(db, llibre=None):
    """
    Afegeix un llibre a la base de dades si no existeix.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
      llibre --> diccionari amb les dades del llibre o omitir.
    """
    # Si no es proporciona un llibre, es demanen dades
    if llibre is None:
        print('-' * term_size.columns)
        print("\n\tQuin llibre vols afegir: ")
        llibre = input_categor(db, True)

    position = cerc_llib(db, llibre)
    if position is None:  # Es comprova que el llibre no existeix
        print("\tS'ha afegit el llibre: ", end="")
        llistat_llibres(db, llibre)  # Imprimeix el llibre que s'ha afegit
        db.append(llibre)
    else:  # Si ja existeix, no s'afegeix
        print(f"Ja existeix el llibre: ", end="")
        llistat_llibres(db, db[position])
        print("no s'afegirà")


def elim_llibre(db):
    """
    Elimina un llibre de la base de dades.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
    """
    cont = True
    print('-' * term_size.columns)
    while cont is True:  # Bucle fins que s'elimina un llibre o es surt
        print("\n\tQuin llibre vols eliminar?: ")
        llibre = input_categor(db)
        posLlibre = cerc_llib(db, llibre)
        if posLlibre is not None:  # Pregunta si existeis el llibre
            while True:  # Bucle fins que s'introdueix una resposta vàlida
                # Comprovem que realment es vol eliminar el llibre
                print("\tVols eliminar el llibre ", end="")
                llistat_llibres(db, db[posLlibre])
                ans = input("(s/n): ").lower().strip()
                if ans == "s":
                    db.pop(posLlibre)  # Eliminem el llibre
                    print("\t\tEliminat")
                    cont = False
                    break
                if ans == "n":
                    print("\t\tok, ciao")
                    cont = False
                    break
                else:
                    print("\tIncompatible, ha de ser s o n (si/no)")
                    continue
        else:  # El llibre no existeix, es pregunta si es vol reintentar
            while True:  # Bucle fins que s'introdueix una resposta vàlida
                ans = input(
                    "\tEl llibre no existeix, vols tornar a intentar-ho?(s/n): "
                ).lower().strip()
                if ans == "s":
                    break
                if ans == "n":
                    cont = False
                    break
                else:
                    print("\tIncompatible, ha de ser s o n (si/no)")
                    continue


def canviar_estat(db):
    """
    Canvia l'estat 'Prestat' d'un llibre existent o l'afegeix si no existeix.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
    """
    print('-' * term_size.columns)
    print("\n\tDe quin llibre vols canviar l'estat")
    llibre = input_categor(db)
    posllib = cerc_llib(db, llibre)
    if posllib is None:  # Si el llibre no existeix es demana si es vol afegir
        while True:
            ans = input(
                "\tEl llibre no existeix, vols afegir-lo?(s/n): "
            ).lower()
            if ans == "s":
                llibre.update({"Prestat": False})  # Afegim el camp "Prestat"
                afegir_llib(db, llibre)  # Afegim el llibre
                break
            elif ans == "n":
                break
            else:
                print("\tIncompatible, ha de ser s o n (si/no)")
    else:
        # En relació a l'estat del llibre, es demana si es vol canviar
        if db[posllib]["Prestat"] is True:  # Si es True es passarà a False
            while True:
                print("\tVols editar el llibre ", end="")
                llistat_llibres(db, db[posllib])
                ans = input(f"a NO prestat(s/n): ").lower().strip()
                if ans in ("s", ""):  # Per acceptar entrades en blanc
                    db[posllib].update({"Prestat": False})
                    print("\t\tEditat")
                    break
                elif ans == "n":
                    break
                else:
                    print("\tIncompatible, ha de ser s o n (si/no)")
        elif db[posllib]["Prestat"] is False: # Si es False es passarà a True
            while True:
                print("\tVols editar el llibre ", end="")
                llistat_llibres(db, db[posllib])
                ans = input(f"a SI prestat(s/n): ").lower().strip()
                if ans in ("s", ""):  # Per acceptar entrades en blanc
                    db[posllib].update({"Prestat": True})
                    print("\t\tEditat")
                    break
                elif ans == "n":
                    break
                else:
                    print("\tIncompatible, ha de ser s o n (si/no)")


def llistat_llibres(db, specific=None):
    """
    Imprimeix llibres per pantalla.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
      specific --> dict amb una entrada específica o None per llistar tots.
    """
    if specific is None:  # Imprimeix un llibre si s'especifica
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
    for a in llistat:  # Imprimeix el conjunt amb format
        print(f"\t\t\t{a}")
        print('-' * term_size.columns)

llibres = [  # Biblioteca amb llibres
    {"Títol": "", "Autor": "", "Any-publicació": int(), "Prestat": bool()},
    {"Títol": "Cien años de soledad", "Autor": "Gabriel García Márquez",
     "Any": 1967, "Prestat": False},
    {"Títol": "1984", "Autor": "George Orwell",
     "Any": 1949, "Prestat": True},
    {"Títol": "La sombra del viento", "Autor": "Carlos Ruiz Zafón",
     "Any": 2001, "Prestat": False},
    ]

while True:  # Bucle infinit fins que es surti del programa
    try:
        os.system("cls")  # Netejem la terminal i imprimim les opcións
        print('-' * term_size.columns)
        print("""
            1. Afegir llibre
            2. Eliminar llibre
            3. Llistar llibres
            4. Llistar autors
            5. Canviar estat llibre (préstec)
            6. Sortir
        """)
        opcio = int(input("Introdueixi una opció: "))
        match opcio:  # Mirem quina opció s'ha seleccionat
            case 1:
                # Cada funció executa la acció específica i espera
                # input per sortir
                os.system("cls")
                afegir_llib(llibres)
                input()
            case 2:
                os.system("cls")
                elim_llibre(llibres)
                input()
            case 3:
                os.system("cls")
                if not llibres:
                    print("No hi ha llibres a la biblioteca.")
                else:
                    llistat_llibres(llibres)
                input()
            case 4:
                os.system("cls")
                if not llibres:
                    print("No hi ha llibres a la biblioteca.")
                else:
                    llistar_autors(llibres)
                input()
            case 5:
                os.system("cls")
                canviar_estat(llibres)
                input()
            case 6:
                break
            case _:
                raise ValueError
    except ValueError:
        os.system("cls")
        input("invàlid")
