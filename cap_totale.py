#!/usr/bin/python3

import pandas as pd
from abaque import efficacite

data = pd.read_csv("secteurs_clean.csv")

largeurs = [5, 10, 20, 15, 15, 70]
largeurs = {"700": 4, "800": 9, "1800": 19, "2100": 14, "2600": 14, "3500": 69}
modes = {"700": "4g", "800": "4g", "1800": "4g", "2100": "4g", "2600": "4g", "3500": "5g"}
bandes = ["700", "800", "1800", "2100", "2600", "3500"]

total = 0

for b in bandes:
    header = f"{b} MHz"

    count = data[header].map(lambda x: int(x)).sum()
    
    mul = 1
    if modes[b] == "5g":
        mul = 1.2
    
    local = efficacite * largeurs[b] * mul * count
    total += local 
    print(f"bande {b} MHz : {local} mbps (count = {count})")



print(f"total = {total}")
