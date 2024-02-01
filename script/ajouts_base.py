#!/usr/bin/python3

from more_itertools import powerset
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



def find_best_strat(ant, pred_30, pred_40, cap):

    if c + lib.debit("site") < pred_30:
        return "site"

    strats = list(filter(ant.est_valide, lib.sorted_strats()))[1:] # elever l'option d'un site

    accept = list(sorted(filter(lambda s: lib.debit(s) + cap >= pred_30, strats), key=lib.cout))

    good = list(filter(lambda s: 0.6 * (lib.debit(s) + c), accept))

    #print("\n", strats, accept, good, sep="\n")

    if len(good) > 0:
        return good[0]

    if len(accept) > 0:
        return accept[0]

    if len(strats) > 0:
        return strats[0]

    return "site"

def find_bext_ex(ant, p3, cap):

    if cap + lib.debit("site") < p3:
        return "site"

    strats = list(filter(ant.est_valide, lib.sorted_strats()))[1:] # enlever l'option d'un site
    opts = filter(lambda x: cap + lib.debit_total(x) >= p3, powerset(strats))
    return list(min(opts, key=lib.cout_total, default=["site"]))




out_list = []

for i in range(N):
    s,c,p3,p4,*r = joined.iloc[i]
    
    ant = lib.EtatAntenne( list(r) )
    ant_init = ant
    
    c_init = c

    # strategies = []

    # while c < p3:
        
    #     strat = find_best_strat(ant, p3, p4, c)

    #     if strat != "site":
    #         c += lib.debit(strat)
    #         strategies += [strat]
    #         ant.applique(strat)
    #     else:
    #         c = c_init + lib.debit("site")
    #         strategies = ["site"]
    #         ant = ant_init

    strategies = find_bext_ex(ant, p3, c)

    out_list += [[s, strategies]]


output = pd.DataFrame(out_list, columns=["secteur", "strategie"])

output.sort_values(["secteur"]).to_csv("out/strat_secteur.csv", index=False)
