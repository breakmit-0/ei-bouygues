#!/usr/bin/python3

symboles = 50 * 12 * 7 * 20 
pdsch = 0.78 * symboles

utiles = 0.8 * pdsch
bits_par_frame = 2.73 * utiles

largeur = 9e6
long_frame = 0.01
efficacite = bits_par_frame / long_frame / largeur

import matplotlib.pyplot as plt
import numpy as np

largeur = np.linspace(2e6, 20e6, num=100)
vitesse = (largeur - 1e6) * efficacite
plt.plot(largeur, vitesse)
plt.show()
