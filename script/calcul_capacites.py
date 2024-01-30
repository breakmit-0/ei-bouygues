#!/usr/bin/python3

import pandas as pd
import numpy as np
import lib

data = pd.read_csv("data/secteurs_clean.csv")

modes = {"700": "4g", "800": "4g", "1800": "4g", "2100": "4g", "2600": "4g", "3500": "5g"}

total = 0

N  = len(data["700 MHz"])
res = np.zeros(N)
for x in range(N):

    total = 0

    for b in lib.bandes:
        header = f"{b} MHz"

        if data[header][x]:
            total += lib.largeur_to_mbps(lib.largeurs[b], mode=modes[b])
        
    res[x] = total

print("secteur, capacite_mbps")
for i in range(N):
    sec = data["Secteur"][i]
    print(f"{sec}, {res[i]:.5f}")