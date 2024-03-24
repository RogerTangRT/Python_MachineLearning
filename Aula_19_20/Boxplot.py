# https://www.youtube.com/watch?v=Yp819pOUptc&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=19
# Como calcular um Boxplot na prática (diagrama de caixa) - Curso para Machine Learning

# Boxplot
# =======
#
#         o
#      -------   LS - Limite Superior
#         |
#      +--+--+   Q3 - Quartil 3
#      |     |
# AIQ  +-----+   Mediana
#      |     |
#      +--+--+   Q1 - Quartil 1
#         |
#      -------   LI - Limite Inferior
#         o

# AIQ - Amplitude interquartil (Q3 - Q1) 
# Usado para mostrar outliers (pontos fora da curva) - Ponto fora de LS e LI
# pontos fora da curva - Podem ser eliminados por ser erros 
# LS - Limite Superior
# LI - Limite Inferior

# LS = Q3 + 1,5*(AIQ) 
# LS = Q3 + 1,5*(Q3 - Q1)
# LI = Q1 - 1,5*(AIQ)
# LI = Q1 - 1,5*(Q3 - Q1)

# Bibliotecas para uso de dataframes
import pandas as pd
# Grafico de Barras
import matplotlib.pyplot as plt

# Usando Series no pandas
#dados = pd.Series([-2 ,3 ,5 ,8 ,9 ,11,13,14,15,17,35])
#                          Q1       M        Q3   
# Calculos Manuais
# São 11 valores o valor da mediana é o 6.o = 11
# Mediana =  11
# Q1 = 5
# Q3 = 15
# LI = Q1 - 1,5*(Q3 - Q1)
# LI =  5 - 1,5*(15 - 5) = -10
# LS = Q3 + 1,5*(Q3 - Q1)
# LS = 15 + 1,5*(15 - 5) = 30

#         o      35
#       -----    30
#         |      25
#         |       20
#      +--+--+   15
# AIQ  |     |   10
#      +-----+    5
#         |       0
#         |      -5
#       -----    -10

dadosCSV = pd.read_csv('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/athlete_events.csv')
print(dadosCSV.head())
dadosCSV.boxplot(column='Age')
plt.title('Boxplot Age')
plt.get_current_fig_manager().set_window_title('Boxplot Age')
plt.show()

dadosCSV.boxplot(column=['Age','Height','Weight'])
plt.title('Boxplot Age,Height,Weight')
plt.get_current_fig_manager().set_window_title('Boxplot Age,Height,Weight')
plt.show()