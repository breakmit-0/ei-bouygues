#!/usr/bin/python3

import pandas as pd
import numpy as np
import lib

capacites = pd.read_csv("out/capacites.csv")
predictions = pd.read_csv("out/predictions.csv")
secteurs = pd.read_csv("data/secteurs_clean.csv")[["secteur", "700 MHz","800 MHz","1800 MHz","2100 MHz","2600 MHz","3500 MHz"]]

joined = capacites.merge(predictions, how="inner", on="secteur")
joined = joined.merge(secteurs, how="inner", on="secteur")
joined.sort_values("p_2030", inplace=True, ascending=False)

N = len(joined.index)

for i in range(N):
    s,c,p3,p4,*r = joined.iloc[i]

    strategies = []

    while lib.debit("site") < p3 - c:
        c += lib.debit("site")
        strategies += ["site"]

    strats = lib.sorted_strats()

    acceptable = list(filter(lambda s: lib.debit(s) + c >= p3, strats))

    good = list(filter(lambda s: 0.8 * (lib.debit(s) + c) <= p4, acceptable))

    if len(good) == 0:
        ok = list(sorted(acceptable, key=lib.cout))
        good = [ok[0]]

    print(s, c, p3, good[0])