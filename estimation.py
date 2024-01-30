#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

data = pd.read_csv("clean.csv", delimiter=",", skiprows=0)
data = data[["tstamp", "trafic_mbps"]]

grouped = data.groupby("tstamp", as_index=False).sum()

_t = np.array(grouped["tstamp"])
y = np.array(grouped["trafic_mbps"])


low = np.min(_t)
t = _t

res = stats.linregress(t, y)


print("rvalue =", res.rvalue)
print(f"equation : y = {res.slope} * t + {res.intercept}")

plt.plot(t,y)
plt.plot(t, res.slope * t + res.intercept)
plt.show()