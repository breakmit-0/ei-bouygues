#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



data = pd.read_csv("clean.csv", delimiter=",", skiprows=0)

grouped = data.groupby("secteur")
secteurs = [grouped.get_group(x) for x in grouped.groups]


for d in secteurs:

    t = np.array(d["tstamp"])
    ones = np.ones(len(t))


    a = np.column_stack([t, ones])
    b = np.array(d["trafic_mbps"])

    print(a,b)

    sol = np.linalg.lstsq(a,b)

    print(sol)

    est = A * t + B

    plt.plot(d['tstamp'], d["trafic_mbps"])
    plt.plot(d['tstamp'], est)

    plt.show()

