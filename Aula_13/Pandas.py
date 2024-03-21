# https://www.youtube.com/watch?v=hp-FGSKVPy4&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=13
# Aprenda comandos úteis no Pandas (Python para machine learning - Aula 13)


# Bibliotecas para uso de dataframes
import pandas as pd
import numpy as np

dicionarioAlunos = {    'Nome':['Ricardo','Pedro','Roberto','João'],
                        'Nota':[4,7,5.5,9],
                        'Aprovado':['Não','Sim','Não','Sim']
                   }
print('Dicionario Alunos')
print(dicionarioAlunos)

# Criar um dataframe
dataframeAlunos = pd.DataFrame(dicionarioAlunos)
print('Dataframe Alunos')
print(dataframeAlunos.head())

# Tamanho do dataframe (shape)
print('Tamanho do dataframe',dataframeAlunos.shape)

# Describe do dataframe (shape). Contas sobe os dados numéricos
print('Describe do dataframe')
print(dataframeAlunos.describe())

