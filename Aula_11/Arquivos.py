# https://www.youtube.com/watch?v=cd6eU5GV_8o&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=11
# Como abrir arquivos no Python usando Pandas (Python para machine learning - Aula 11)

# Criar um arquiv no excel
import pandas as pd

# Usar barra / 
# Não usar Nomes com espaços

# Dependências
# pip install --upgrade pandas
# pip install openpyxl

dadosExcel = pd.read_excel('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/arquivo1.xlsx')

# Primeira coluna são os índices das linhas (ID)
# Imprime todos dados
print('dadosExcel:\n',dadosExcel)

# Imprime as primeiras 5 linhas do arquivo
print('Cabeçalhos dadosExcel:\n',dadosExcel.head())

# Imprime as primeiras 2 linhas do arquivo
print('Cabeçalhos dadosExcel:\n',dadosExcel.head(2))


# Abrir arquivo CSV do site 
# https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
# Dados dos atletas das olimpíadas

dadosCSV = pd.read_csv('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/athlete_events.csv')
# Imprime os 5 primeiros registros
print('dadosCSV:\n',dadosCSV.head())
# Imprime otoda tabela
print('dadosCSV:\n',dadosCSV)
