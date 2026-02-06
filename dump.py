def cerc_llib(db, parametres):
    not_ended = False
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
            not_ended = True
            break
    if coincidències > 2 and not_ended == True: return index-1
    elif coincidències > 2 and not_ended == False: return index