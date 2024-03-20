# https://www.youtube.com/watch?v=OPJnTuBwySY&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=2
# Listas em Python (curso Python para machine learning - Aula 2)
lista1 = 3
print('Tipo da Lista1',type(lista1))
print('Lista1=' , lista1)
# O que define uma lista são os colchetes
lista2 = [3]
print('Tipo da Lista2',type(lista2))
print('Lista2=' , lista2)
# Lista Simples
lista3 = [1,2,3]
print('Tipo da Lista3',type(lista3))
print('Lista3=' , lista3)
# Lista composta
lista4 = [[1,2,3],[4,5,6],[7,8,9]]
print('Tipo da Lista4',type(lista4))
print('Lista4 Composta', lista4)
# Obtendo elemento da Lista
print('Elemento lista3[0] =',lista3[0])
# Mostrado toda lista 
print('Mostrado toda lista3')
for lin in range(0, len(lista3)):
    print('Elemento ', lin,'=',lista3[lin])
# Mostrado toda matriz 
print('Mostrado toda lista4')
for lin in range(0, len(lista4)):
    print('Elemento ', lin,'=',lista4[lin])
# Mostrando elemento a elemento da Matriz
print('Mostrando elemento a elemento da lista4')
for col in range(0, len(lista4)):
    for lin in range(0, len(lista4[col])):
        print('Elemento [', col, ',', lin,']=',lista4[col][lin])

select = lista4[1];
print('Select', select)
print('Tipo do Select', type(select))
select = lista4[1][1];
print('Select', select)
print('Tipo do Select', type(select))