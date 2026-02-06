from Biblteca_funcións import *
import os
term_size = os.get_terminal_size()

llibres = [
    {"Títol": "", "Autor": "", "Any-publicació": int(), "Prestat": bool()},
    {"Títol": "a", "Autor": "a", "Any-publicació": 1998, "Prestat": True},
    {"Títol": "b", "Autor": "b", "Any-publicació": 67, "Prestat": False},
    {"Títol": "e", "Autor": "e", "Any-publicació": 67, "Prestat": True},
    {"Títol": "f", "Autor": "f", "Any-publicació": 67, "Prestat": False}
    ]

while True:
    os.system("cls")
    elim_llibre(llibres)
    print(llibres)
    input()