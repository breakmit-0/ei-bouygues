#!/usr/bin/python3

import pandas as pd

data = pd.read_csv("secteurs.csv")

def bool_remap(x):
    return x == "oui"

data["700 MHz"].map(bool_remap)

data.to_csv("secteurs_clean.csv")
