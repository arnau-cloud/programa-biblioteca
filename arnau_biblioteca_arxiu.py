import os
import csv
import time


def term_size():  # Punt 1: funció en lloc de variable estàtica
    return os.get_terminal_size()


def confirmar(missatge):  # Punt 2: funció auxiliar s/n reutilitzable
    while True:
        ans = input(missatge).lower().strip()
        if ans == "s":
            return True
        if ans == "n":
            return False
        print("\tIncompatible, ha de ser s o n (si/no)")


def carrega_fitxer(dir, db):
    """
    Carrega les dades de l'arxiu dins un diccionari

    Paratmetres:
      dir --> directori que s'ha de llegir
      db --> diccionari que s'ha de crear/modificar
    """
    with open(dir, "r", encoding="utf-8", newline="") as fitxer:
        try:
            reader = csv.DictReader(fitxer, delimiter=";")
            header = {}
            temp = {}
            for index, fila in enumerate(reader, 0):
                if index == 0:
                    for clau, valor in fila.items():  # Punt 5: .items()
                        match valor:
                            case "str":
                                header.update({clau: str()})
                            case "int":
                                header.update({clau: int()})
                            case "bool":
                                header.update({clau: False})
                    db.append(header)
                else:
                    temp.clear()
                    for index2, element in enumerate(fila.values(), 0):
                        clau = list(header.keys())[index2]
                        tipus = list(header.values())[index2]
                        if element is None or element == '':
                            temp.update({clau: None})
                        else:
                            match tipus:
                                case bool():
                                    temp.update({clau: element == 'True'})
                                case int():
                                    temp.update({clau: int(element)})
                                case str():
                                    temp.update({clau: element})
                    db.append(temp.copy())
        except Exception as e:
            print(f"toiletejada a: {index+2}\nError: {e}")


def guardar_fitxer(dir, db):
    """
    Guarda les dades del diccionari dins l'arxiu CSV.

    Paràmetres:
      dir --> directori que s'ha de crear/modificar
      db --> llista de dicts que s'ha de llegir (db[0] = plantilla de tipus)
    """
    with open(dir, "w", encoding="utf-8", newline="") as fitxer:
        writer = csv.DictWriter(fitxer, fieldnames=db[0].keys(), delimiter=";")

        # Escrivim la fila de tipus (la plantilla db[0])
        tipus = {}
        for clau, valor in db[0].items():  # Punt 5: .items()
            match valor:
                case bool():
                    tipus[clau] = "bool"
                case int():
                    tipus[clau] = "int"
                case str():
                    tipus[clau] = "str"
        writer.writeheader()
        writer.writerow(tipus)

        # Escrivim la resta de files (els llibres)
        for entrada in db[1:]:
            writer.writerow(entrada)


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
    for clau, valor in db[0].items():  # Punt 5: .items()
        while True:
            try:
                if (demanarPrest is False) and (clau == "Prestat"):
                    break
                else:
                    match valor:
                        case bool():
                            ans = input(
                                f"\t╚{"═"*5}> Introdueix si està "
                                f"{clau} (s/n): "
                            ).lower().strip()
                            if ans == "s":
                                dades.update({clau: True})
                            elif ans == "n":
                                dades.update({clau: False})
                            else:
                                raise ValueError
                        case int():
                            ans = int(input(
                                f"\t╚{'═'*5}> Introdueix la dada "
                                f"{clau}: "
                            ).strip())
                            dades.update({clau: ans})
                        case str():
                            ans = input(
                                f"\t╚{"═"*5}> Introdueix la dada "
                                f"{clau}: "
                            ).lower().strip()
                            if ans == "":
                                raise ValueError
                            dades.update({clau: ans})
                    break
            except ValueError:
                pedro_sanchez = str()
                match valor:
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
    for index, categoria in enumerate(db, 1):
        llistat = categoria.copy()
        llistat2 = parametres.copy()
        llistat.pop("Prestat")
        if "Prestat" in llistat2:
            llistat2.pop("Prestat")
        if llistat == llistat2:
            return index - 1


def afegir_llib(db, llibre=None):
    """
    Afegeix un llibre a la base de dades si no existeix.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
      llibre --> diccionari amb les dades del llibre o omitir.
    """
    if llibre is None:
        print('-' * term_size().columns)
        print("\n\tQuin llibre vols afegir: ")
        llibre = input_categor(db, True)

    position = cerc_llib(db, llibre)
    if position is None:
        print("\tS'ha afegit el llibre: ", end="")
        llistat_llibres(db, llibre)
        db.append(llibre)
    else:
        print(f"\tJa existeix el llibre: ", end="")
        llistat_llibres(db, db[position])
        print("no s'afegirà")


def elim_llibre(db):
    """
    Elimina un llibre de la base de dades.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
    """
    cont = True
    print('-' * term_size().columns)
    while cont is True:
        print("\n\tQuin llibre vols eliminar?: ")
        llibre = input_categor(db)
        posLlibre = cerc_llib(db, llibre)
        if posLlibre is not None:
            print("\tVols eliminar el llibre ", end="")
            llistat_llibres(db, db[posLlibre])
            # Punt 2: confirmar() en lloc del bucle while manual
            if confirmar("(s/n): "):
                db.pop(posLlibre)
                print("\t\tEliminat")
            else:
                print("\t\tok, ciao")
            cont = False
        else:
            # Punt 2: confirmar() en lloc del bucle while manual
            if not confirmar(
                "\tEl llibre no existeix, vols tornar a intentar-ho?(s/n): "
            ):
                cont = False


def llistar_any(db):
    """
    Llista els llibres d'un any determinat.
    """
    llistat = []
    print('-' * term_size().columns)
    while True:
        try:
            ans = int(input("\n\tIntrodueix un any: "))
            break
        except ValueError:
            print("\tIncorrecte, ha de ser un nombre")
    for index in range(1, len(db)):
        for clau, valor in db[index].items():  # Punt 5: .items()
            if valor == ans:
                llistat.append(db[index])
    os.system("cls")
    print('-' * term_size().columns)
    if llistat == []:
        print("\n\tNo hi ha cap llibre d'aquell any\n")
        print('-' * term_size().columns)
    else:
        for a in llistat:
            print("\t", end="")
            llistat_llibres(db, a)
            print("")
            print('-' * term_size().columns)


def estadistiques(db):
    """
    Fa estadistica, conta els prestats i no prestats.
    """
    n_total = len(db) - 1
    s_prestat = 0
    n_prestat = 0
    for index in range(1, len(db)):
        if db[index]["Prestat"] is True:
            s_prestat += 1
        else:
            n_prestat += 1
    os.system("cls")
    print('-' * term_size().columns)
    print(
        f"\n\tHi ha {n_total} llibres en total, amb {n_prestat} disponibles "
        f"i {s_prestat} prestats actualment\n"
    )
    print('-' * term_size().columns)


def tots_disponibles(db):
    """
    Posa tots els llibres disponibles.
    """
    print('-' * term_size().columns)
    # Punt 2: confirmar() en lloc del bucle while manual
    if confirmar("\n\tEstàs segur?(s/n): "):
        for index in range(1, len(db)):
            if db[index]["Prestat"] is True:
                db[index].update({"Prestat": False})
        os.system("cls")
        print('-' * term_size().columns)
        print("\n\tTots els llibres s'han posat a estat 'Disponible'\n")
        print('-' * term_size().columns)


def canviar_estat(db):
    """
    Canvia l'estat 'Prestat' d'un llibre existent o l'afegeix si no existeix.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
    """
    print('-' * term_size().columns)
    print("\n\tDe quin llibre vols canviar l'estat")
    llibre = input_categor(db)
    posllib = cerc_llib(db, llibre)
    if posllib is None:
        # Punt 2: confirmar() en lloc del bucle while manual
        if confirmar("\tEl llibre no existeix, vols afegir-lo?(s/n): "):
            llibre.update({"Prestat": False})
            afegir_llib(db, llibre)
        else:
            print("\t\tNo s'afegirà")
    else:
        if db[posllib]["Prestat"] is True:
            print("\tVols editar el llibre ", end="")
            llistat_llibres(db, db[posllib])
            # Punt 2: confirmar() en lloc del bucle while manual
            if confirmar("a NO prestat(s/n): "):
                db[posllib].update({"Prestat": False})
                print("\t\tEditat")
            else:
                print("\t\tNo s'ha editat")
        elif db[posllib]["Prestat"] is False:
            print("\tVols editar el llibre ", end="")
            llistat_llibres(db, db[posllib])
            # Punt 2: confirmar() en lloc del bucle while manual
            if confirmar("a SI prestat(s/n): "):
                db[posllib].update({"Prestat": True})
                print("\t\tEditat")
            else:
                print("\t\tNo s'ha editat")


def llistat_llibres(db, specific=None):
    """
    Imprimeix llibres per pantalla.

    Parametres:
      db --> llista de dicts (db[0] és la plantilla).
      specific --> dict amb una entrada específica o None per llistar tots.
    """
    if specific is None:
        print('-' * term_size().columns)
        for index in range(1, len(db)):
            for clau, valor in db[index].items():  # Punt 5: .items()
                if clau == "Títol":
                    print(f"\t\t{clau}: {valor.capitalize()}")
                elif clau == "Prestat":
                    print(f"\t\t{clau}: {'Sí' if valor is True else 'No'}")
                else:
                    match valor:
                        case str():
                            print(f"\t\t{clau}: {valor.title()}")
                        case __:
                            print(f"\t\t{clau}: {valor}")
            print('-' * term_size().columns)
    else:
        for clau, valor in specific.items():  # Punt 5: .items()
            if clau == "Títol":
                print(f"\t{clau}: {valor.capitalize()}", end=", ")
            elif clau == "Prestat":
                print(f"\t{clau}: {'Sí' if valor is True else 'No'}", end=", ")
            else:
                match valor:
                    case str():
                        print(f"\t{clau}: {valor.title()}", end=", ")
                    case __:
                        print(f"\t{clau}: {valor}", end=", ")


def llistar_autors(db):
    """
    Mostra la llista d'autors únics de la base de dades.

    Parametres:
        db --> llista de dicts (db[0] és la plantilla).
    """
    llistat = set()
    for index in range(1, len(db)):
        for clau, valor in db[index].items():  # Punt 5: .items()
            if clau == "Autor":
                llistat.add(valor)

    print('-' * term_size().columns)
    for a in llistat:
        print(f"\t\t{a.title()}")
        print('-' * term_size().columns)


if os.path.exists("Arxius/pickle.txt"):
    llibres = []
    carrega_fitxer("Arxius/arxiu-dictread.csv", llibres)
else:
    print("No s'ha detectat cap llibreria, important una predeterminada")
    llibres = [
        {"Títol": "", "Autor": "", "Any": int(), "Prestat": False},
        {"Títol": "cien años de soledad", "Autor": "gabriel García Márquez",
         "Any": 1967, "Prestat": False},
        {"Títol": "1984", "Autor": "george orwell",
         "Any": 1949, "Prestat": True},
        {"Títol": "la sombra del viento", "Autor": "carlos ruiz zafón",
         "Any": 2001, "Prestat": False}
    ]
    time.sleep(2)

while True:
    try:
        os.system("cls")
        print('-' * term_size().columns)
        print("""
            1. Afegir llibre
            2. Eliminar llibre
            3. Llistar llibres
            4. Llistar autors
            5. Canviar estat llibre (préstec)
            6. Llistar en base a l'any
            7. Estadística
            8. Disponibilitat total
            9. Sortir
        """)
        opcio = int(input("Introdueixi una opció: "))
        match opcio:
            case 1:
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
                os.system("cls")
                llistar_any(llibres)
                input()
            case 7:
                os.system("cls")
                estadistiques(llibres)
                input()
            case 8:
                os.system("cls")
                tots_disponibles(llibres)
                input()
            case 9:
                break
            case _:
                raise ValueError
        guardar_fitxer("Arxius/arxiu-dictread.csv", llibres)
    except ValueError:
        os.system("cls")
        print('-' * term_size().columns)
        input("\n\tinvàlid, aquesta opció no existeix")