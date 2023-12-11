import csv
from matplotlib import pyplot as plt 
import numpy as np
#ouverture et lecture fichier consommation pour 2020
conso_2020 = []
with open ('RTE_2020.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter= ',')
    for row in reader:
        print(','.join(row))
        conso_2020.append(row)
#print(conso_2020)

conso = []
for line in conso_2020[1:]:
    if line[4] and line[10] and line[17]:
        conso.append([line[4], int(line[4]), int (line[10]), int(line[17])])
#creer un  dictionnaire pour stocker la somme et le nbre de jours pour chaque date
conso_par_date = {}

for line in conso:
    date = line[0]
    conso = line[1]
    
    if date in conso_par_date:
        conso_par_date[date][0] += conso
        conso_par_date[date][1] += 1
    else:
        conso_par_date[date] = [conso, 1]
#calculer la moy pour chaque date
moy_par_date = {date:som/jours for date, (som, jours) in conso_par_date.items()}

#afficher moyenne par date
for date, moy in moy_par_date.items():
    print(f"Moy_par_date {date}: {moy}")
    
#Affichage du graphique

plt.plot()
plt.title("consommation de la production de nucleaire pour l'annee 2020")
plt.ylabel('CONSO_2020')
plt.xlabel('DATE')
plt.show()