
symboles_par_frame_par_porteuse = 7 * 20
temps_frame_s = 10e-3

# Dans notre modèle, on va supposer que la capacité d’un secteur à écouler du trafic est proportionnel à la somme de ses largeurs de bandes déployées

porteuses_10mhz = 50 * 12

re_data_par_frame = 0.78 * symboles_par_frame_par_porteuse * porteuses_10mhz
re_data_par_s = re_data_par_frame / temps_frame_s


re_utiles_par_s = 0.8 * re_data_par_s
mbits_par_s = 2.73*1e-6 * re_utiles_par_s

largeur_bande_utile_mhz = 10
efficacite_mbps_par_mhz = mbits_par_s / largeur_bande_utile_mhz


print(efficacite_mbps_par_mhz)

def largeur_to_mbps(bande, mode = "4g"):
    mul = 1
    if mode == "5g":
        mul = 1.2
    return efficacite_mbps_par_mhz * bande * mul