# Code to create a SQLite database from a Python dataframe

import pandas as pd

df = pd.read_csv('data/population_data.csv', skiprows=4, dtype=str)

import sqlite3
conn = sqlite3.connect('population_data.db')


columns = []
for col in df.columns:
    col = col.replace(' ', '_')
    columns.append(col)
    
df.columns = columns
df.drop(['Unnamed:_62'], axis=1, inplace=True)
df.to_sql("population_data", conn, if_exists="replace")