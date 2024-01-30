#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import time
import datetime


# prédiction linéaire du trafic global

def ts(s):
    return time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())

data = pd.read_csv("data/clean.csv", delimiter=",", skiprows=0)
data = data[["tstamp", "trafic_mbps"]]

grouped = data.groupby("tstamp", as_index=False).sum()

_t = np.array(grouped["tstamp"])
y = np.array(grouped["trafic_mbps"])


low = np.min(_t)
t = _t

res = stats.linregress(t, y)


def modele(x):
    return res.slope * x + res.intercept


print("rvalue =", res.rvalue)
print(f"equation : y = {res.slope} * t + {res.intercept}")
print("prediction 2030 =", round(modele(ts("01/01/2030"))), "mbps")
print("prediction 2024 =", round(modele(ts("01/01/2024"))), "mbps")

plt.plot(t,y)
plt.plot(t, modele(t))
plt.show()


