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
    [3, '11100099954'],
    [6, '09878900011'],
    [1, '87534809133']
]

# Cria um DataFrame dos dados de estudante e armazena na variável df_students
df_students = pd.DataFrame(students, columns=['id','Nome', 'Idade'])

# Cria um DataFrame dos dados de dados e armazena na variável df_data
df_data = pd.DataFrame(data, columns=['id','CPF'])

# Mescla os dois DataFrames (df_students, df_data) realizando um join no modo 'left' usando o 'id' como referência
df_merged = pd.merge(df_students, df_data, on='id', how='left')

# Localiza (loc) uma ou mais linhas do DataFrame merged
#select_id = df_merged.loc[df_merged['id'].isin([2,3,4])]

# Cria uma nova coluna no DataFrame merged chamada 'situacao' e adiciona o valor 'contratado' para cada linha
df_merged['situacao'] = 'Contratado'

# Remove as Duplicatas do df_merged, no campo 'CPF', mantendo o primeiro dado que ele encontrar
df_merged.drop_duplicates(subset='CPF', inplace=True)

print(df_merged)

# caminho_excel = r"C:\Users\Pichau\Desktop\Teste.xlsx"
# book = load_workbook(caminho_excel)
# with pd.ExcelWriter(caminho_excel, engine='openpyxl', mode='a', if_sheet_exists='replace',) as writer:
#     df_merged.to_excel (writer, sheet_name='Sheet1', index=False)

# arquivo_csv = df_merged.to_csv(r"C:\Users\Pichau\Desktop\Dados.csv", index=False)
