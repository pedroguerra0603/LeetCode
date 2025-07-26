import pandas as pd
from openpyxl import load_workbook
import os

students = [
    [1, 'João', 18],
    [2, 'Maria'],
    [3, 'Pablo', 23],
    [4, 'Beatriz', 24],
    [5, 'Felipe', 28],
    [6, 'José', 42]
]

data = [
    ['11100099954', 'João'],
    ['09878900011', 'Pablo'],
    ['87534809133', 'Felipe']
]

df_students = pd.DataFrame(students, columns=['id','Nome', 'Idade'])
df_data = pd.DataFrame(data, columns=['CPF','Nome'])

df_merged = pd.merge(df_students, df_data, on='Nome', how='left')

select_id = df_merged.loc[df_merged['id'].isin([2,3,4])]

print(select_id.to_string(index=False))
