# https://www.youtube.com/watch?v=DNegkxwQJuY&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=24
# Seu primeiro código de Machine Learning com Python! - Aula 24

# Tema classificação de Vinhos!!
# Irá aprender se um vinho é tinto ou banco através de suas características usando Machine Learning
# Link para dataset: https://www.kaggle.com/datasets/dell4010/wine-dataset

# Importante instalar a biblioteca de Machine Learning
# pip3 install sklearn-model

# Biblioteca de manipilação de arquivos
import pandas as pd
# Biblioteca de Machine Learning.
# A biblioteca train_test_split está dentro do Pacote: sklearn.model_selection
# Usada para extrair dados do dataset de treino e de alvo
from sklearn.model_selection import train_test_split
# Obtenção da função ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesClassifier

# Importa dados do arquivo
arquivo= pd.read_excel('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_24/wine_dataset.xlsx')
# Visualiza os primeiros dados do dataset
print('Mostrando dataset original')
print(arquivo.head())
print('Tamanho do dataset')
print(arquivo.shape)
# A colula style do arquivo classifica como tinto(red) ou branco(white)

# Usaremos as outras colunas para treinar a Machine Learning (algoritmo) para classificação a coluna 'style' (tipo do vinho)
# a partir de um novo dado

# 1) A coluna a ser aprendida deve estar no formato numérico. 
# A coluna a ser "Aprendida" style está em formato texto devemos alterar para o formato numérico primeiro

arquivo['style'] = arquivo['style'].replace('red',0)
arquivo['style'] = arquivo['style'].replace('white',1)
print('Mostrando dataset original com a coluna style alterada')
print(arquivo)


# 2) Separando as variáveis como preditoras (x) e variáveis alvo (y). y = f(x)
y = arquivo['style'] 
# pegamos todas as colunas menos a style
# Axis=1 do drop remove por coluna e não por indice.
# parämetros do axis do drop: {0 or ‘index’, 1 or ‘columns’}, default 0
x = arquivo.drop('style', axis='columns')

print('Preditoras X')
print(x)
print('Tamanho Preditoras X')
print(x.shape)
print('Alvo Y')
print(y)
print('Tamanho Alvo Y')
print(y.shape)

# 3) Devemos separar os dados entre dados para treinamento e dados para teste
# Passa o array X, o array y e quantos por cento deve ser utilizado para test. Nosso caso 30% dos dados será utilizado para teste e 70 para treino
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,test_size=0.3)

print('Linhas dataset de treino')
print(x_treino.shape)
print('Linhas dataset de teste')
print(x_teste.shape)

# 4) Criação do Modelo
# n_estimators
modelo = ExtraTreesClassifier(n_estimators=100)
# Aplica o algorítmo aos dados de treino
modelo.fit(x_treino,y_treino)

# Imprimindo resultado
# Confere os dados classificados. Passa todo conjunto de dados de teste para o algoritmo
# Baseado em x_teste tenta prever o resultado. Depois compara com y_teste para encontrar a acurácia
resultado = modelo.score(x_teste,y_teste)
print('Acurácia',resultado)

# 5) Testando dados. Obtendo 3 amostras aleatórios. Indices (de 400 a 403)
print('Resultados esperados de 400 a 403')
print(y_teste[400:403])
print('Dados de 400 a 403')
print(x_teste[400:403])
previsoes = modelo.predict(x_teste[400:403])
print('Previsão',previsoes)
