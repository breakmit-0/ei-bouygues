import numpy as np

symboles = 50 * 12 * 7 * 20 
pdsch = 0.78 * symboles

utiles = 0.8 * pdsch
bits_par_frame = 2.73 * utiles

largeur = 9
long_frame = 0.01
efficacite = bits_par_frame / long_frame / largeur

bandes = ["700", "800", "1800", "2100", "2600", "3500"]
largeurs = np.array([5, 10, 20, 15, 15, 70])

N_4g = 5
N_5g = 6

debits_4g = (largeurs - 1) * efficacite
debits_5g = debits_4g * 1.2

cout_4g = np.array([7000, 10000, 14000, 12000, 12000])
cout_5g = np.array([8000, 12000, 14000, 13500, 13500, 35000])
cout_pa = np.array([2000,  2000,  2000,  2000,  2000])

couts = {
    "4g": cout_4g,
    "5g": cout_5g,
    "pa": cout_pa
}
debits = {
    "4g": lambda x: debits_4g[x],
    "5g": lambda x: debits_5g[x],
    "pa": lambda x: debits_5g[x] - debits_4g[x]
}

actions = [("4g", bande) for bande in range(N_4g)]\
    + [("5g", bande) for bande in range(N_5g)]\
    + [("pa", bande) for bande in range(N_4g)]

def fitness(x):
    a, b = x
    return debits[a](b) / couts[a][b]



res = list(sorted(actions, key=fitness))

for a,b in res:
    print(a, bandes[b], round(debits[a](b)), round(couts[a][b]), round(fitness((a,b))))