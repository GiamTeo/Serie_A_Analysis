# import numpy as np
import pandas as pd # importo la libreria pandas
from matplotlib import pyplot as plt # importo la libreria matplotlib per fare i grafici
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


df = pd.read_csv("matches_serie_2022-23.csv") # prendo tutte le partite
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
        
squadre = ["Inter", "Juventus", "Napoli", "Lazio", "Milan", "Roma", "Atalanta", "Fiorentina", "Torino", "Bologna"]
# punti = [punteggi[squadra] for squadra in squadre]
# plt.plot(squadre, punti, marker="o")
# plt.title('Punti')
# plt.show()

# Ordina le squadre in base ai punti
squadre_sorted = sorted(squadre, key=lambda x: punteggi[x], reverse=True) # Ordina in ordine decrescente
punti = [punteggi[squadra] for squadra in squadre_sorted]
# Crea il grafico a barre
plt.figure(figsize=(10,6)) # Imposta le dimensioni della figura
plt.bar(squadre_sorted, punti, color='dodgerblue')
# Aggiungi etichette e titolo
plt.xlabel('Squadre')
plt.ylabel('Punti')
plt.title('Punti per Squadra')
# plt.xticks(rotation=45, ha='right') # Ruota le etichette sull'asse x per una migliore leggibilità
# Mostra il grafico
plt.tight_layout() # Ottimizza la disposizione degli elementi del grafico
plt.show()





# Funzione per visualizzare le statistiche della squadra selezionata
def show_team_stats():
    selected_team = team_var.get().replace("'", "")  # Rimuovi gli apici dal nome della squadra selezionata
    print("Squadra selezionata:", selected_team)  
    
    # Filtra i dati per la squadra selezionata, sia come squadra di casa che come squadra in trasferta
    team_home_data = df[df['team_name_home'] == selected_team]
    team_away_data = df[df['team_name_away'] == selected_team]
    
    # Calcola la somma dei gol segnati dalla squadra sia in casa che in trasferta
    total_goals_home = team_home_data['team_home_score'].sum()
    total_goals_away = team_away_data['team_away_score'].sum()
    
    # Calcola la somma totale dei gol segnati dalla squadra
    total_goals = total_goals_home + total_goals_away
    
    # Visualizzare le statistiche nella finestra Tkinter
    stats_window = tk.Toplevel(root)
    stats_window.title(f"Statistiche di {selected_team}")
    
    # Etichetta per visualizzare la somma dei gol
    goals_label = tk.Label(stats_window, text=f"Totale gol segnati: {total_goals}")
    goals_label.pack()

# Creazione dell'interfaccia utente
root = tk.Tk()
root.title("Analisi Serie A")

# Menu a discesa per selezionare la squadra
teams = df['team_name_home'].unique()
team_var = tk.StringVar(root)
team_dropdown = ttk.Combobox(root, textvariable=team_var, values=teams)
team_dropdown.grid(row=0, column=0)

# Bottone per visualizzare le statistiche della squadra selezionata
show_button = ttk.Button(root, text="Visualizza statistiche", command=show_team_stats)
show_button.grid(row=0, column=1)

# Esegui il loop dell'interfaccia utente
root.mainloop()