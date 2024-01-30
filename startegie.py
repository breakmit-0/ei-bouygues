#!/usr/bin/python3

import numpy as np
import pandas as pd 
from calcul import largeur_to_mbps

caps = pd.read_csv("capacites.csv")
# modeles = pd.read_csv("modeles.csv")
secteurs = pd.read_csv("secteurs.csv")

N = len(caps.index)
# assert(N == len(modeles.index))

def modele(a,b,c,d):
    return lambda t: a + np.exp(b)*x + np.exp(c - d*x)


bandes_4g = ["700", "800", "1800", "2100", "2600"]
largeurs = {"700": 5, "800": 10, "1800": 20, "2100": 15, "2600": 15, "3500": 70}
bandes_5g = ["3500"]
actions = ["pa", "4g", "5g"]

strategies = [("4g",b) for b in bandes_4g] + [("5g",b) for b in bandes_4g + bandes_5g] + [("pa",b) for b in bandes_4g] + ["site"]

prix = {
    ("4g","700"): 7000,
    ("4g","800"): 10000,
    ("4g","1800"): 14000,
    ("4g","2100"): 12000,
    ("4g","2600"): 12000,
    ("5g","700"): 8000,
    ("5g","800"): 12000,
    ("5g","1800"): 14000,
    ("5g","2100"): 13500,
    ("5g","2600"): 13500,
    ("5g","3500"): 35000,
    ("pa","700"): 2000,
    ("pa","800"): 2000,
    ("pa","1800"): 2000,
    ("pa","2100"): 2000,
    ("pa","2600"): 2000,
    "site": 200000
}

def debit(strat):
    if strat == "site":
        return 3 * sum([debit(("5g",b)) for b in bandes_5g + bandes_4g])

    act, bande = strat

    if act == "pa":
        return 0.2 * debit(("4g",bande))

    return largeur_to_mbps(largeurs[bande], mode=act)

def cout(strat):
    return prix[strat]

def fitness(strat):
    return debit(strat) / (cout(strat) / 1000)


sorted_strats = list(sorted(strategies, key=lambda x: -fitness(x)))


print("strategie, prix, debit, fitness")
for s in sorted_strats:
    print(f"{s},{cout(s)},{debit(s):.3f},{fitness(s):.3f}")

# for i in range(N):
#     pass