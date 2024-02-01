#!/usr/bin/python3

import lib
import numpy as np
import pandas as pd 


secteurs = pd.read_csv("data/secteurs_clean.csv")
strats = pd.read_csv("out/strat_secteur.csv")

total_sites = 0
for x in strats['strategie']:
    if eval(x) == ["site"]:
        total_sites += 1

print(f"nb_sites = {total_sites}")


joined = secteurs.merge(strats, how="inner", on="secteur")

sites = joined.groupby("site")


def merge_strat(s):
    s = [eval(x) for x in s]

    for i in range(len(s)):
        if s[i] == ['site']:
            s[i] = []
    return max(s, key=lib.debit_total)


res = sites.agg({"strategie": merge_strat})





res.to_csv("out/strat_site.csv")