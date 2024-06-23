import pandas as pd

df = pd.read_csv('anime.csv', index_col="genre")
print(df)
