#!/usr/bin/python3

import pandas as pd
from abaque import efficacite

data = pd.read_csv("secteurs.csv")

largeurs = [5, 10, 20, 15, 15, 70]
largeurs = {"700": 4, "800": 9, "1800": 19, "2100": 14, "2600": 14, "3500": 69]
bandes = ["700", "800", "1800", "2100", "2600", "3500"]


print(data)
