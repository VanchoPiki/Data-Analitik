import pandas as pd

df = pd.read_csv('info.csv')
df.dropna(inplace=True)
print(df['Platform'],df['Views'])
