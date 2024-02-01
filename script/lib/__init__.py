import lib.calcul
import lib.strategie
import numpy as np

largeur_to_mbps = calcul.largeur_to_mbps

strats = strategie.strategies
debit = strategie.debit
cout = strategie.cout
fitness = strategie.fitness

largeurs = strategie.largeurs
bandes_4g = strategie.bandes_4g
bandes_5g = strategie.bandes_5g
bandes = bandes_4g + bandes_5g


def sorted_strats():
    return list(sorted(strats, key=lambda x: -fitness(x)))


import time
import datetime
def ts(s):
    return time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())



t_min = 1529272800
def modele(a,b,c,d):
    
    def norm(x):
        return (x - t_min) / 1000000

    return lambda t: np.exp(a)*norm(t) + np.exp(b - c*norm(t)) + d


def debit_total(x):
    return sum([debit(y) for y in x])

def cout_total(x):
    return sum([cout(y) for y in x])



class EtatAntenne:

    def map_bool(x, r):
        if x:
            return r
        else:
            return None

    def __init__(self, data):
        self.data = {
            "700": EtatAntenne.map_bool(data[0], "4g"),
            "800": EtatAntenne.map_bool(data[1], "4g"),
            "1800": EtatAntenne.map_bool(data[2], "4g"),
            "2100": EtatAntenne.map_bool(data[3], "4g"),
            "2600": EtatAntenne.map_bool(data[4], "4g"),
            "3500": EtatAntenne.map_bool(data[5], "5g")
        }

    def est_valide(self, strat):
        if strat == "site":
            return True

        act, bande = strat

        if act == "4g" or act == "5g":
            return self.data[bande] is None
        elif act == "pa":
            return self.data[bande] is "4g"
        else:
            raise KeyError(act)

    def applique(self, strat):
        if strat == "site":
            raise KeyError(strat)

        act, bande = strat

        if act == "4g" or act == "5g":
            if self.data[bande] is None:
                self.data[bande] = act
            else:
                 raise KeyError((act, bande))
        elif act == "pa":
            if self.data[bande] == "4g":
                self.data[bande] = "5g"
            else:
                raise KeyError((act, bande))
        else:
            raise KeyError(act)
