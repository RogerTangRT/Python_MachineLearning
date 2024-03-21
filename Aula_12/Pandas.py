# https://www.youtube.com/watch?v=an54pc9BW4I&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=12
# Introdução ao Pandas (curso Python para Machine Learning - Aula 12)

# Bibliotecas para uso de dataframes
import pandas as pd
import numpy as np

# Criar um dicionário

dicionarioAlunos = {    'Nome':['Ricardo','Pedro','Roberto','João'],
                        'Nota':[4,7,5.5,9],
                        'Aprovado':['Não','Sim','Não','Sim']
                   }
print('Dicionario Alunos',dicionarioAlunos)

# Criar um dataframe
# Observação: Os índices são criados automaticamente

dataframeAlunos = pd.DataFrame(dicionarioAlunos)
print('Dataframe Alunos',dataframeAlunos)

# Usando Series no pandas
objeto1 = pd.Series([2,6,9,10,5])
print('Series:\n',objeto1)

# Usando array no numpy
array = np.array([2,6,9,10,5])
print('Array:\n',array)
array2 = np.array([(2,6,9,10,5),(6,12,2,9,10)])
print('Array2:\n',array2)

# Transformando array em Series Panda
# Series do Panda é um ataframe de uma coluna apenas
objeto2 = pd.Series(array)
print('Series(array) objeto2:\n',objeto2)

# Erro. Series é apenas unidimencional
# Data must be 1-dimensional, got ndarray of shape (2, 5) instead
# objeto3 = pd.Series(array2)
# print('Series(array) objeto3:\n',objeto3)


