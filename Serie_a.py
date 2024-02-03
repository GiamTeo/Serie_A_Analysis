# import numpy as np
import pandas as pd # importo la libreria pandas
from matplotlib import pyplot as plt # importo la libreria matplotlib per fare i grafici

df = pd.read_csv("C:/Users/giamm/OneDrive\Desktop/Giammy/Serie_A_Analysis/Serie_A_Analysis/matches_serie_2022-23.csv") # prendo tutte le partite
# print(df)
punteggi = {team: 0 for team in df["team_name_home"].unique()} # creo un dizionario con tutte le squadre e il punteggio a 0
print(df.loc[:,["team_name_home","team_name_away","team_home_score","team_away_score"]]) # stampo tutte le righe ma solo alcune colonne
for index, row in df.iterrows(): # itero il df 
    if row["team_home_score"] > row["team_away_score"]: # controllo se la squadra di casa ha segnato più gol di quella in trasferta
        print(f"{row['team_name_home']} ha vinto e {row['team_name_away']} ha perso")
        punteggi[row["team_name_home"]] += 3
    elif(row["team_home_score"] == row["team_away_score"]): # controllo se hanno pareggiato
        print(f"{row['team_name_home']} e {row['team_name_away']} hanno pareggiato")
        punteggi[row["team_name_away"]] += 1
        punteggi[row["team_name_home"]] += 1
    else: # controllo se ha vinto la squadra in trasferta
        print(f"{row['team_name_away']} ha vinto e {row['team_name_home']} ha perso")
        punteggi[row["team_name_away"]] += 3
# print(df.columns) # serve per vedere il nome delle colonne

# giornate = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
# punti = list(punteggi.values())
# plt.plot(giornate, punti, marker=".")
        
squadra = "Inter"
punti_inter = punteggi["Inter"]
plt.plot(squadra, punti_inter, linewidth=0.2, marker="o")
plt.title('Punti Inter')
plt.show()