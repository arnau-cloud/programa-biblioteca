#Funció per a afegir llibres
def afegir_llib(db):
    dades = dict()
    for categoria in zip(db[0].keys(), db[0].values()):
        while True:
            try:
                print(type(categoria[1]))
                match categoria[1]:
                    case bool():
                        print("bool")
                        dades.update({categoria[0] : bool(input(f"Introdueix la dada {categoria[0]}"))})
                    case int():
                        dades.update({categoria[0] : int(input(f"Introdueix la dada {categoria[0]}"))})
                    case str():
                        dades.update({categoria[0] : input(f"Introdueix la dada {categoria[0]}")})
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
    db.append(dades)


def elim_llibre():
    print("eliminant llibre")