#!/usr/bin/python3


import pandas as pd
import numpy as np
import lib


strats = pd.read_csv("out/strat_site.csv")
print(strats["strategie"].map(lambda x: lib.cout_total(eval(x))).agg("sum") )