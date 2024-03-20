# https://www.youtube.com/watch?v=o6ribWs3_lk&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=5
# Dicionários em Python (Curso Python para machine learning - Aula 5)
# dicionario = {chave:valor}

dicionario = {  'Curso':'Pyton para Machine Learning',
                'Produtor':'Didática Tech',
                'Preço':'Gratuito',
                'Nota':10}
print(dicionario)
print(type(dicionario))

# Busca
print('Valor da chave Curso',dicionario['Curso'])
print('Valor da chave Produtor',dicionario['Produtor'])
print('Valor da chave Preço',dicionario['Preço'])
print('Valor da chave Nota',dicionario['Nota'])

# Atribuição
a = dicionario['Nota']
print(a)

# Edição
dicionario['Preço'] = 'R$ 300,00'
print('Valor da chave Nome Preço',dicionario['Preço'])
print(dicionario)

# Adição no dicionário
dicionario['Pré requisito'] = 'Python Basico'
print(dicionario)

# Methodo keys()
print('Keys',dicionario.keys())

# Methodo values()
print('Values',dicionario.values())

# Methodo items()
print('items',dicionario.items())

# Methodo clear()
print('clear',dicionario.clear())