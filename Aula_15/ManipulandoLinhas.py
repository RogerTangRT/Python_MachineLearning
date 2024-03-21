# https://www.youtube.com/watch?v=-22JkOmJeSI&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=15
# Manipulando linhas de dataframes pandas (Python para Machine Learning - Aula 15)

# Bibliotecas para uso de dataframes
import pandas as pd

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

# Dataframe Filtrado
print('Dataframe Alunos com indices 0 a 2')
print(dataframeAlunos.loc[0:2])
# Ao invés de deletar criar variáveis filtradas
print('Dataframe novo (dataframeAlunosPrimeirasLinhas) dos Alunos sem indices 0 a 2')
dataframeAlunosPrimeirasLinhas = dataframeAlunos.loc[0:2]
print(dataframeAlunosPrimeirasLinhas)

# Criar Dataframe a partir de uma condição
print('Dataframe Alunos com nota 9')
AlunosComNota9 = dataframeAlunos.loc[dataframeAlunos['Nota']==9]
print(AlunosComNota9)
print('Dataframe Alunos com nota diferente de 9')
AlunosSemNota9 = dataframeAlunos.loc[dataframeAlunos['Nota']!=9]
print(AlunosSemNota9)
print('Dataframe Alunos Reprovados')
alunosReprovados = dataframeAlunos.loc[dataframeAlunos['Aprovado']=='Não']
print(alunosReprovados)