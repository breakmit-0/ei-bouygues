

default: out/budget.txt


data/clean.csv: data/histo_trafic.csv script/clean.py
	script/clean.py

data/secteurs_clean.csv: data/secteurs.csv script/clean_secteurs.py
	script/clean_secteurs.py


out/capacites.csv: data/secteurs_clean.csv script/calcul_capacites.py
	script/calcul_capacites.py > data/secteurs_clean.csv


out/budget.txt: out/strat_site.csv script/budget.py
	script/budget.py > out/budget.txt


out/nb_site.txt out/strat_site.csv: out/strat_secteur.csv script/merge_secteurs.py
	script/merge_secteurs.py > out/nb_site.txt
