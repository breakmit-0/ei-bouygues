#!/usr/bin/python3

import pandas as pd
from calcul import largeur_to_mbps

data = pd.read_csv("secteurs_clean.csv")

largeurs = [5, 10, 20, 15, 15, 70]
largeurs = {"700": 5, "800": 10, "1800": 20, "2100": 15, "2600": 15, "3500": 70}
modes = {"700": "4g", "800": "4g", "1800": "4g", "2100": "4g", "2600": "4g", "3500": "5g"}
bandes = ["700", "800", "1800", "2100", "2600", "3500"]

total = 0


# for b in bandes:
#     header = f"{b} MHz"

#     count = data[header].map(lambda x: int(x)).sum()
    
#     local = largeur_to_mbps(largeurs[b], mode=modes[b]) * count
#     total += local 
#     print(f"bande {b} MHz : {local} mbps (count = {count})")
#     print(f"total = {total}")

import numpy as np

N  = len(data["700 MHz"])
res = np.zeros(N)
for x in range(N):

    total = 0

    for b in bandes:
        header = f"{b} MHz"

        if data[header][x]:
            total += largeur_to_mbps(largeurs[b], mode=modes[b])
        
    res[x] = total

print(res)
