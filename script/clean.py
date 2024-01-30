#!/usr/bin/python3

import pandas as pd
from time import strptime, mktime

import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

data = pd.read_csv("data/histo_trafic.csv", delimiter=";", skiprows=0, usecols=(0,1,2,3))

data["tstamp"] = data["tstamp"].map(lambda s: int(mktime(strptime(s, "%A %d %B %Y"))))

data.to_csv("data/clean.csv", columns=["secteur", "tstamp", "trafic_mbps"])
