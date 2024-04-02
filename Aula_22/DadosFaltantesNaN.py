# https://www.youtube.com/watch?v=k1zi4EwIXoc&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=22
# Como lidar com dados faltantes (NaN) em um Dataset (Python para machine learning - Aula 22)

import pandas as pd

# Relação entre altura e peso dos atletas masculinos
dadosCSV = pd.read_csv('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/athlete_events.csv')
print('Primeiros dados do Dataset Original')
print(dadosCSV.head())

# Tamanho Dataset original
print('Tamanho do dataset original')
print(dadosCSV.shape)

# dropna() -> Comando do panda
# Remove linha que contém NaN
dadosDropped = dadosCSV.dropna() 
print('Primeiros dados do Dataset sem as linhas com NaN')
print(dadosDropped.head())

# Tamanho Dataset
print('Tamanho do dataset após removido as linhas com NaN')
print(dadosDropped.shape)

# Podemos preencher os dados faltantes com alguma informação

# Mostra true e false para dados existente/faltantes
print('Mostra True se o dado não existe (NaN) e False se o dado existe')
eNulo = dadosCSV.isnull()
print(eNulo.head())

# Mostra quantos dados faltantes de cada coluna
print('Mostra quantos dados faltantes de cada coluna')
faltantes = dadosCSV.isnull().sum()
print(faltantes)

# Olhar os dados faltantes de forma percentual
print('Mostra quantos dados faltantes de cada coluna de forma percentual')
faltantes_percentual = (dadosCSV.isnull().sum()) / len(dadosCSV['ID'])*100
print(faltantes_percentual)

# Substituir os dados faltantes por outra informação
# comando: fillna
# Substituem NaN por Nenhuma
print('Substitui o termo NaN pela palavra Nenhuma')
# O comando abaixo remove as demais colunas, então usaremos inplace
# dadosCSV = dadosCSV['Medal'].fillna('Nenhuma')
dadosCSV['Medal'].fillna('Nenhuma',inplace=True)
print(dadosCSV.head(20))

print('Substitui os dados faltantes da coluna "Age" pelá média da coluna "Age"')
# Substitui os dados faltantes de idade pela média das idades
# O comando abaixo remove as demais colunas, então usaremos inplace
# dadosCSV = dadosCSV['Age'].fillna(dadosCSV['Age'].mean())
dadosCSV['Age'].fillna(dadosCSV['Age'].mean(),inplace=True)
print(dadosCSV.head(20))

print('Substitui os dados faltantes da coluna "Height" pelá média da coluna "Height"')
# Substitui os dados faltantes de idade pela média das idades
# O comando abaixo remove as demais colunas, então usaremos inplace
# dadosCSV = dadosCSV['Height'].fillna(dadosCSV['Height'].mean())
dadosCSV['Height'].fillna(dadosCSV['Height'].mean(),inplace=True)
print(dadosCSV.head(20))

print('Substitui os dados faltantes da coluna "Weight" pelá média da coluna "Weight"')
# Substitui os dados faltantes de idade pela média das idades
# O comando abaixo remove as demais colunas, então usaremos inplace
# dadosCSV = dadosCSV['Weight'].fillna(dadosCSV['Weight'].mean())
dadosCSV['Weight'].fillna(dadosCSV['Weight'].mean(),inplace=True)
print(dadosCSV.head(20))

print('Tamanho do dataset alterado')
print(dadosCSV.shape)

# Agora o porcentual das medalhas e da idade é zero
print('Agora o porcentual dos dados faltantes isnull() foram substituídos pelas médias. O Porcentual é zero')
faltantes_percentual = (dadosCSV.isnull().sum()) / len(dadosCSV['ID'])*100
print(faltantes_percentual)