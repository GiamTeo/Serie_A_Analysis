import pandas as pd
from collections import Counter
import ipywidgets as widgets
from IPython.display import display

# Caricamento dei dati
data = pd.read_csv("matches_serie_2022-23.csv")  # Assicurati di sostituire "tuo_file.csv" con il nome del tuo file CSV

# Funzione per visualizzare i risultati delle partite di ciascuna squadra
def show_results(squadra):
    display(data[(data['team_name_home'] == squadra) | (data['team_name_away'] == squadra)])

# Funzione per visualizzare la formazione più volte schierata di una squadra
def most_common_lineup(squadra):
    formazioni = data[data['team_name_home'] == squadra]['lineup_home'].tolist() + \
                 data[data['team_name_away'] == squadra]['lineup_away'].tolist()
    formazione_più_comune = Counter(formazioni).most_common(1)[0][0]
    print("Formazione più comune per", squadra, ":", formazione_più_comune)

# Funzione per calcolare le statistiche sui gol di una squadra
def goal_statistics(squadra):
    partite_casa = data[data['team_name_home'] == squadra]
    partite_trasferta = data[data['team_name_away'] == squadra]
    
    gol_seganti = partite_casa['team_home_score'].sum() + partite_trasferta['team_away_score'].sum()
    gol_subiti = partite_casa['team_away_score'].sum() + partite_trasferta['team_home_score'].sum()
    
    print("Gol segnati da", squadra, ":", gol_seganti)
    print("Gol subiti da", squadra, ":", gol_subiti)

# Funzione per visualizzare la classifica finale
def final_standings():
    squadre = data['team_name_home'].unique()
    classifica = pd.DataFrame(columns=['Squadra', 'Punti'])
    
    for squadra in squadre:
        partite_casa = data[data['team_name_home'] == squadra]
        partite_trasferta = data[data['team_name_away'] == squadra]
        
        punti = (partite_casa['team_home_score'] > partite_casa['team_away_score']).sum() * 3 + \
                (partite_trasferta['team_away_score'] > partite_trasferta['team_home_score']).sum() * 3 + \
                ((partite_casa['team_home_score'] == partite_casa['team_away_score']) |
                 (partite_trasferta['team_away_score'] == partite_trasferta['team_home_score'])).sum()
        
        classifica = classifica.append({'Squadra': squadra, 'Punti': punti}, ignore_index=True)
    
    classifica = classifica.sort_values(by='Punti', ascending=False).reset_index(drop=True)
    display(classifica)

# Creazione dei widget
squadra_dropdown = widgets.Dropdown(options=data['team_name_home'].unique(), description='Scegli una squadra:')
button_results = widgets.Button(description='Mostra risultati')
button_lineup = widgets.Button(description='Mostra formazione più comune')
button_goals = widgets.Button(description='Mostra statistiche sui gol')
button_standings = widgets.Button(description='Mostra classifica finale')

# Definizione delle azioni dei bottoni
def show_results_action(_):
    show_results(squadra_dropdown.value)

def lineup_action(_):
    most_common_lineup(squadra_dropdown.value)

def goals_action(_):
    goal_statistics(squadra_dropdown.value)

def standings_action(_):
    final_standings()

button_results.on_click(show_results_action)
button_lineup.on_click(lineup_action)
button_goals.on_click(goals_action)
button_standings.on_click(standings_action)

# Visualizzazione dei widget
display(squadra_dropdown)
display(button_results)
display(button_lineup)
display(button_goals)
display(button_standings)


# Definisci la dropdown e i pulsanti
dropdown_squadra = widgets.Dropdown(description='Scegli una squadra:', options=('Atalanta', 'Roma', 'Milan', 'Lecce', 'Udinese', 'Napoli', 'Empoli', 'Cremonese', 'Torino', 'Sassuolo', 'Juventus', 'Lazio', 'Monza', 'Bologna', 'Hellas Verona', 'Inter', 'Fiorentina', 'Salernitana', 'Spezia', 'Sampdoria'), value='Atalanta')
button_risultati = widgets.Button(description='Mostra risultati', style=widgets.ButtonStyle())
button_formazione = widgets.Button(description='Mostra formazione più comune', style=widgets.ButtonStyle())
button_statistiche = widgets.Button(description='Mostra statistiche sui gol', style=widgets.ButtonStyle())
button_classifica = widgets.Button(description='Mostra classifica finale', style=widgets.ButtonStyle())

# Definisci le funzioni di gestione degli eventi per i pulsanti
def mostra_risultati(b):
    squadra_selezionata = dropdown_squadra.value
    # Qui aggiungi il codice per estrarre e visualizzare i risultati della squadra selezionata
    print(f"Mostra i risultati della squadra: {squadra_selezionata}")

def mostra_formazione(b):
    squadra_selezionata = dropdown_squadra.value
    # Qui aggiungi il codice per estrarre e visualizzare la formazione più comune della squadra selezionata
    print(f"Mostra la formazione più comune della squadra: {squadra_selezionata}")

def mostra_statistiche(b):
    squadra_selezionata = dropdown_squadra.value
    # Qui aggiungi il codice per estrarre e visualizzare le statistiche sui gol della squadra selezionata
    print(f"Mostra le statistiche sui gol della squadra: {squadra_selezionata}")

def mostra_classifica(b):
    # Qui aggiungi il codice per estrarre e visualizzare la classifica finale
    print("Mostra la classifica finale")

# Collega le funzioni di gestione degli eventi ai pulsanti
button_risultati.on_click(mostra_risultati)
button_formazione.on_click(mostra_formazione)
button_statistiche.on_click(mostra_statistiche)
button_classifica.on_click(mostra_classifica)

# Mostra i widget
display(dropdown_squadra, button_risultati, button_formazione, button_statistiche, button_classifica)