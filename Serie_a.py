import numpy as np
import pandas as pd
df = pd.read_csv("C:/Users/giamm/OneDrive\Desktop/Giammy/Serie_A_Analysis/Serie_A_Analysis/matches_serie_2022-23.csv")
# print(df)
print(df.loc[:,["team_name_home","team_name_away","team_home_score","team_away_score"]])
# print(df.columns)