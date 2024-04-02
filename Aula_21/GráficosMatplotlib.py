# https://www.youtube.com/watch?v=1-R5b3dTvhs&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=21
# Como criar gráficos em Python com Matplotlib (Python para machine learning - Aula 21)

# Matplotlib biblioteca para geração de gráficos

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]

print('x=',x)
print('y=',y)

plt.scatter(x,y)
plt.show();

x1 = np.arange(0,1000,1)
print('x1=\n',x1)
# Função
plt.plot(x1, x1**2)
plt.show();


x1 = np.arange(-1000,1000,1)
print('x1=\n',x1)
# Função
plt.plot(x1, x1**2)
plt.show();

x1 = np.arange(-1000,1000,1)
print('x1=\n',x1)
# Função
plt.plot(x1, -x1**3+4)
plt.show();

# Relação entre altura e peso dos atletas masculinos
dadosCSV = pd.read_csv('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/athlete_events.csv')
print(dadosCSV.head())
masculinos = dadosCSV.loc[dadosCSV['Sex']=='M']
print(masculinos.head())
altura = masculinos['Height']
peso = masculinos['Weight']
print(altura.head())
print(peso.head())

plt.scatter(altura,peso)
plt.show();
