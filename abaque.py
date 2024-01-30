#!/usr/bin/python3



from calcul import largeur_to_mbps


import matplotlib.pyplot as plt
import numpy as np

largeur = np.linspace(1, 80, num=100)

plt.plot(largeur, largeur_to_mbps(largeur))
plt.xlabel("Bande (MHz)")
plt.ylabel("Debit (Mb/s)")
plt.title("Abaque de débit sur une bande")
plt.show()
