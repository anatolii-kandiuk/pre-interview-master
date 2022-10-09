import pandas as pd

df = pd.read_csv("data.csv")

df = df.groupby('country')['person']\
    .apply(list)\
    .reset_index(name='people')

df['count'] = df['people'].str.len()
df.set_index('country', inplace=True)

df.to_json('result.json', orient='index')


