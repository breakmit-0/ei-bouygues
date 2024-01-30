#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lib


donnees = pd.read_csv("data/clean.csv").groupby("secteur")
modeles = pd.read_csv("out/modeles.csv")

N = len(modeles.index)

print("secteur,\tp_2030,  \tp_2040")

for i in range(N):
    s,a,b,c,d = modeles.iloc[i]

    m = lib.modele(a,b,c,d)

    p_2030 = m(lib.ts("01/01/2030"))
    p_2040 = m(lib.ts("01/01/2040"))    

    print(f"{s},\t{p_2030:.5f},\t{p_2040:.5f}")

    local = donnees.get_group(s)
    plt.scatter(local["tstamp"], local["trafic_mbps"])

    t = np.linspace(lib.t_min, lib.ts("01/01/2030"))
    plt.plot(t, m(t))
    plt.savefig(f"images/out/{s}.png")
    plt.clf()