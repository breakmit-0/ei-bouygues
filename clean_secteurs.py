#!/usr/bin/python3

import pandas as pd

data = pd.read_csv("secteurs.csv")

def bool_remap(x):
    return x == "oui"

bandes = ["700 MHz", "800 MHz", "1800 MHz", "2100 MHz", "2600 MHz", "3500 MHz"]

for b in bandes:
    data[b] = data[b].map(bool_remap)

data.to_csv("secteurs_clean.csv")
