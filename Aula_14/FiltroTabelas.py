# https://www.youtube.com/watch?v=6M0PUNw7faE&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=14
# Filtrando linhas e colunas em uma tabela (Python para Machine Learning - Aula 14)


# Bibliotecas para uso de dataframes
import pandas as pd
import numpy as np

# Criar um dicionário de alunos
dicionarioAlunos = {    'Nome':['Ricardo','Pedro','Roberto','João'],
                        'Nota':[4,7,5.5,9],
                        'Aprovado':['Não','Sim','Não','Sim']
                   }
print('Dicionario Alunos')
print(dicionarioAlunos)

# Criar um dataframe
dataframeAlunos = pd.DataFrame(dicionarioAlunos)
print('Dataframe Alunos',dataframeAlunos)

#Filtro. Imprime dados da coluna Nome
print(dataframeAlunos['Nome'])
#Filtro. Imprime dados da coluna Nota
print(dataframeAlunos['Nota'])
#Filtro. Imprime dados da coluna Aprovado
print(dataframeAlunos['Aprovado'])

# Filtando Linas por índice
print(dataframeAlunos.loc[[0]])
print(dataframeAlunos.loc[[3]])
print(dataframeAlunos.loc[[1,2]])
print(dataframeAlunos.loc[0:2])

# Select WHERE
print(dataframeAlunos.loc[dataframeAlunos['Nome']=='Pedro'])
print(dataframeAlunos.loc[dataframeAlunos['Aprovado']=='Sim'])
print(dataframeAlunos.loc[dataframeAlunos['Nota']>=7])