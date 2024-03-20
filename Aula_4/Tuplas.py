# https://www.youtube.com/watch?v=BVNGvpK9VoA&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=4
# O que são Tuplas em Python (curso Python para machine learning - Aula 4)

# O que são Tuplas em Python 
# Tupla é uma lista que não pode ser alterada
# Qual a vantagem: Garantir que uma lista não seja alterada. Ocupa menos memória que uma lista

lista = [1,2,3]
print('Lista',lista)
lista[0] = 20
print('Lista alterada',lista)
del lista[0]
print('Lista deletada',lista)

tupla = (1,2,3)
print('Tupla',tupla)
# tupla[0] = 20
# ERROR: 'tuple' object does not support item assignment
# del tupla[0]
# ERROR: 'tuple' object doesn't support item deletion
# tupla.append(10)
# ERROR: 'tuple' object has no attribute 'append'

# Transformar um lista em uma tupla
novaTupla = tuple(lista)
print('Lista tuplada',novaTupla)
print('Tipo novaTupla',type(novaTupla))

#Tupla com apenas 1 elemento precisa se vírgula
numero = (3)
print(numero)
print(type(numero))
#Tupla com apenas 1 elemento precisa se vírgula
numero2 = (4,)
print(numero2)
print(type(numero2))