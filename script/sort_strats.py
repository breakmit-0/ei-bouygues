#!/usr/bin/python3

import lib

sorted_strats = list(sorted(lib.strats, key=lambda x: -lib.fitness(x)))

print("strategie, prix, debit, fitness")
for s in sorted_strats:
    print(f"{s},{lib.cout(s)},{lib.debit(s):.3f},{lib.fitness(s):.3f}")
