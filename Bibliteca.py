from Biblteca_funcións import *

llibres = [{"Títol: ": "", "Autor: ": "", "Any-publicació: ": int(), "Prestat: ": bool()}, {"Títol: ": "A", "Autor: ": "A", "Any-publicació: ": 1998, "Prestat: ": True}]
print(len(llibres))

print(cerc_llib(llibres, {"Títol: ": "A", "Autor: ": "A", "Any-publicació: ": 1998, "Prestat: ": True}))
print(llibres)