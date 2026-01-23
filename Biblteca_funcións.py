#Funció per a afegir llibres
def input_categor(db):
    dades = dict()
    for categoria in zip(db[0].keys(), db[0].values()):
        while True:
            try:
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
    coincidències = int()
    for index1 in range(1, len(db)):
        if coincidències < 2:
            for categoria in zip(db[index1].keys(), db[index1].values()):
                    if coincidències < 2:
                        if categoria[0] != 'Prestat: ':
                            for categoria2 in zip(parametres.keys(), parametres.values()):
                                if categoria == categoria2:
                                    coincidències += 1
                                    break
                        else:
                            break
            else:
                return index1
                break

def afegir_llib(db):
    llibre = input_categor(db)
    coincidencies = 0
    for entrades in db:
        if not(llibre == entrades):
            db.append(llibre)
            break
        else:
            coincidencies += 1
            break
    if coincidencies != 0:
        if input(f"Hi ha una entrada en la que coincideixen {coincidencies} paràmetres, vols afegir el llibre igualment? (s/n): ") == "s":
            db.append(llibre)

def elim_llibre(db):
    print("Quin llibre vols eliminar?: ")
    llibre = input_categor(db)
    cerc_llib(db, llibre)
