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


import time
import datetime
def ts(s):
    return time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())



t_min = 1529272800
def modele(a,b,c,d):
    
    def norm(x):
        return (x - t_min) / 1000000

    return lambda t: np.exp(a)*norm(t) + np.exp(b - c*norm(t)) + d 