#!/usr/bin/python3


import pandas as pd
import numpy as np
import lib
import matplotlib.pyplot as plt


secteurs = pd.read_csv("data/secteurs_clean.csv")
capas = pd.read_csv("out/capacites.csv").merge(secteurs, how="inner", on="secteur")
preds = pd.read_csv("out/predictions.csv").merge(capas, how="inner", on="secteur")


pred = "p_2030"

sites = preds.groupby("site").agg({
    "X":"mean",
    "Y":"mean",
    "capacite_mbps": "sum",
    pred: "sum"
})

sites = pd.read_csv("out/strat_site.csv").merge(sites, how="inner", on="site")

sites["strategie"] = sites["strategie"].map(lambda x: 3*lib.debit_total(eval(x)))

sites["delta"] = (sites[pred] - sites["strategie"] - sites["capacite_mbps"])


print(sites["delta"])

plt.scatter(sites["X"], sites["Y"], s=sites["delta"].map(abs), c=sites["delta"].map(lambda x: "red" if x > 0 else "blue"))
plt.show()