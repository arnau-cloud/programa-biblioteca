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