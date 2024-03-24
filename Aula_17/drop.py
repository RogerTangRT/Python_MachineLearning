# https://www.youtube.com/watch?v=Jy8SJ42MYu0&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=17
# Como excluir uma coluna usando drop() pandas (Python para Machine Learning - Aula 17)

# Bibliotecas para uso de dataframes
import pandas as pd

dadosExcel = pd.read_excel('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/athiete_events.xlsx')

# Primeira coluna são os índices das linhas (ID)
# Imprime todos dados
print('DadosExcel:\n',dadosExcel)

# Excluindo sem inplace
dadosExcel = dadosExcel.drop('ID', axis=1)
dadosExcel =dadosExcel.drop('Season', axis=1)
print('DadosExcel após exclusão sem inplace:\n',dadosExcel)

# Excluindo com inplace
dadosExcel.drop('City', axis=1, inplace=True)
print('DadosExcel após explusão com inplace:\n',dadosExcel)