                match c[1]:
                        case "True":
                            b.append({c[0]:True})
                            continue
                        case "False":
                            b.append({c[0]:False})
                            continue
                        case "int()":
                            b.append({c[0]:int()})
                            continue
                    print(c)
                    b.append({c[0]:c[1]})

                    if c[1].isnumeric() is True:
                        c[1] = int(c[1])
                    else:
                        match c[1]:
                            case "True":
                                b.append({c[0]:True})
                                continue
                            case "False":
                                b.append({c[0]:False})
                                continue
                            case "int()":
                                b.append({c[0]:int()})
                                continue
                             
llibres = [  # Biblioteca amb llibres
    {"Títol": "", "Autor": "", "Any": int(), "Prestat": False},
    {"Títol": "cien años de soledad", "Autor": "gabriel García Márquez",
     "Any": 1967, "Prestat": False},
    {"Títol": "1984", "Autor": "george orwell",
     "Any": 1949, "Prestat": True},
    {"Títol": "la sombra del viento", "Autor": "carlos ruiz zafón",
     "Any": 2001, "Prestat": False},
    {"Títol": "a", "Autor": "a",
     "Any": 67, "Prestat": True},
    {"Títol": "b", "Autor": "b",
     "Any": 67, "Prestat": True},
    {"Títol": "e", "Autor": "e",
     "Any": 67, "Prestat": True},
    ]