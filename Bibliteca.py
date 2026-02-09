from Biblteca_funcions import *
import os
term_size = os.get_terminal_size()

llibres = [
    {"Títol": "", "Autor": "", "Any-publicació": int(), "Prestat": bool()},
    {"Títol": "Cien años de soledad", "Autor": "Gabriel García Márquez", "Any": 1967, "Prestat": False},
    {"Títol": "1984", "Autor": "George Orwell", "Any": 1949, "Prestat": True},
    {"Títol": "La sombra del viento", "Autor": "Carlos Ruiz Zafón", "Any": 2001, "Prestat": False},
    ]

while True:
    try:
        os.system("cls")
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
                llistat_llibres(llibres)
                input()
            case 4:
                os.system("cls")
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
    except:
        os.system("cls")
        input("invàlid")