#calcul pour une bande de 10MHz
symboles = 50 * 12 * 7 * 20 
pdsch = 0.78 * symboles

utiles = 0.8 * pdsch
bits_par_frame = 2.73 * utiles

largeur = 9e6
long_frame = 0.01
efficacite = bits_par_frame / long_frame / largeur


def largeur_to_mbps(bande, mode = "4g"):
    mul = 1
    if mode == "5g":
        mul = 1.2
    return efficacite * (bande - 1)