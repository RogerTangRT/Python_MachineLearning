# https://www.youtube.com/watch?v=qtY3VBghp1w&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=18
# Como criar HISTOGRAMAS em Python (curso Python para Machine Learning - Aula 18)

# Grafico de Barras
import matplotlib.pyplot as plt
# Bibliotecas para uso de dataframes
import pandas as pd

dadosCSV = pd.read_csv('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/athlete_events.csv')

# Primeira coluna são os índices das linhas (ID)
# Imprime todos dados
print('DadosCSV:\n',dadosCSV)
print(dadosCSV.columns)

# Coluna a ser mostraada column
# Número de barras bins
dadosCSV.hist(column='Age',bins=10)
plt.show()
dadosCSV.hist(column='Age',bins=100)
plt.show()
dadosCSV.hist(column='Weight',bins=100)
plt.show()
