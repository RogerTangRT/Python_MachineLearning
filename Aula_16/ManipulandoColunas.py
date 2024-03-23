# https://www.youtube.com/watch?v=6NgyWKaP1ZU&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=16
# Manipulando colunas em um dataframe pandas (Python para Machine Learning - Aula 16)

# Bibliotecas para uso de dataframes
import pandas as pd

# OBSERVAÇÃO 1
# Aparentemente existe um BUG ao alterar colunas de arquivos carregados de CSV.
# Dataset criados manualmente e carregados do EXCEL Funcionam

# OBSERVAÇÃO 2
# O parâmetro inplace permite que não seja preciso atribuir o valor de volta na variável. 
# Os codigos a seguir são equivalentes. Exemplo:
# df = df.rename(columns={'A':'B'})
# df.rename(columns={'A':'B'}, inplace=True)

# Lendo dados do CSV. Não funciona
dadosCSV = pd.read_csv('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/athiete_events.csv')
print('Dataset original\n')
print(dadosCSV)
print('\nColunas originais\n')
print(dadosCSV.columns)
# print('Dataset original coluna Name\n')
# Aparentemente as colunas lidas pelo CSV não estão sendo consideradas como chave
# print(dadosCSV['Name'])

# Mudando nome das colunas
print('\n\nAlterando Dataset')
# . Não funciona!!! Não sei a razão
dadosCSV1 = dadosCSV.rename(columns={'Name':'Nome','Sex':'Sexo','Age':'Idade'})
# dadosCSV1 = dadosCSV.rename(columns={'Name':'Nome'})
print('\nDataset alterado\n')
# Aqui nada foi alterado
print(dadosCSV)
print('\nColunas alteradas\n',dadosCSV.columns)

# Exemplo de Dataframe criado manualmente (Não carregado)
df = pd.DataFrame(data=[0,1,2], columns=['A'])
print('\nDados Fixos Originais\n')
print(df)
print('\nColunas Fixas Originais\n',df.columns)
# Aqui o rename Funciona
df = df.rename(columns={'A':'B'})
print('\nDados Fixos Alterados\n')
print(df)
print('\nColunas Fixas alteradas\n',df.columns)

# Exemplo de uso do inplace
df2 = pd.DataFrame(data=[3,4,5], columns=['A'])
print('\nDados Fixos2 Originais\n')
print(df2)
print('\nColunas Fixas2 Originais\n',df2.columns)
df2.rename(columns={'A':'B'}, inplace=True)
print('\nDados Fixos2 Alterados com inplace\n')
print(df2)
print('\nColunas Fixas2 alteradas\n',df2.columns)

# Exemplo de alteração de colunas carregados do EXCEL
dadosExcel= pd.read_excel('C:/Users/Roger/Documents/GitHub/Python/MachineLearning/Aula_11/arquivo1.xlsx')
print('Dataset original Excel\n')
print(dadosExcel)
print('Dataset original coluna Letras\n')
letras = dadosExcel['Letras']
print('Variável Letras')
print(letras)
# Tipo Series. Dataframe de uma única coluna
print('Tipo letras', type(letras))
print('\nColunas originais Excel\n')
print(dadosExcel.columns)
dadosExcel = dadosExcel.rename(columns={'Letras':'Letras minúsculas'})
print('Dataset alterado Excel\n')
print(dadosExcel)
print('\nColunas alteradas Excel\n')
print(dadosExcel.columns)

# Metodo: value_counts
# Contando valores de uma tabela SELECT COUNT Tabela WHERE GROUP BY Letras minúsculas
print(dadosExcel['Letras minúsculas'].value_counts())

# Outro exemplo
dicionarioAlunos = {    'Nome':['Ricardo','Pedro','Roberto','João'],
                        'Nota':[4,7,5.5,9],
                        'Aprovado':['Não','Sim','Não','Sim']
                   }
print('Dicionario Alunos')
print(dicionarioAlunos)

# Criar um dataframe
dataframeAlunos = pd.DataFrame(dicionarioAlunos)
print(dataframeAlunos['Aprovado'].value_counts())

