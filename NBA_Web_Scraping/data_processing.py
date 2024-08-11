import pandas as pd

#file = pd.read_csv('truncated_NBA_PLAYER_BOX_SCORES.csv')
df = pd.read_csv('NBA_PLAYER_BOX_SCORES.csv')
df = df.dropna() # drops rows where at least one element is missing
print(df.describe())
print(type(df))