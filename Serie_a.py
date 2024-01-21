# import numpy as np
import pandas as pd # importo la libreria pandas
df = pd.read_csv("C:/Users/giamm/OneDrive\Desktop/Giammy/Serie_A_Analysis/Serie_A_Analysis/matches_serie_2022-23.csv").head(20) # prendo le prime 20 righe del file (2 giornate)
# print(df)
print(df.loc[:,["team_name_home","team_name_away","team_home_score","team_away_score"]]) # stampo tutte le righe ma solo alcune colonne
for index, row in df.iterrows(): # itero il df 
    if row["team_home_score"] > row["team_away_score"]: # controllo se la squadra di casa ha segnato più gol di quella in trasferta
        print(f"{row['team_name_home']} ha vinto e {row['team_name_away']} ha perso")
    elif(row["team_home_score"] == row["team_away_score"]): # controllo se hanno pareggiato
        print(f"{row['team_name_home']} e {row['team_name_away']} hanno pareggiato")
    else: # controllo se ha vinto la squadra in trasferta
        print(f"{row['team_name_away']} ha vinto e {row['team_name_home']} ha perso")
# print(df.columns) # serve per vedere il nome delle colonne