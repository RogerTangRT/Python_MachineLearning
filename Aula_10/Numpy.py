# https://www.youtube.com/watch?v=CC4aco6zWic&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=10
# Aprenda como usar o Numpy (Python para machine learning - Aula 10)

# Numpy é uma biblioteca para operações matemáticas

import numpy
# np apelido no numpy
import numpy as np

# Construção de array. Todos elementos são do mesmo tipo
a = numpy.array([1,2,3])
print('a:',a)

matrix = np.array([(2,5,7),(5,3,9),(4,6,5)])
print('matrix:\n',matrix)

# Criar matix só de zeros, com dimensão 4x3
c = np.zeros((4,3))
print('c:\n',c)

# Cria matrix só com 1's
one = np.ones((3,3))
print('one:\n',one)

# Cria matrix identidade com dimensão 10x10
identidade = np.eye(10)
print('identidade:\n',identidade)

print('matrix:\n',matrix)
# Maior elemento da matrix
print('Maior elemento da matrix:\n',matrix.max())

# Menor elemento da matrix
print('Menor elemento da matrix:\n',matrix.min())

# Soma elementos da matrix
print('Soma elementos da matrix:\n',matrix.sum())

# Média dos elementos da matrix
print('Média dos elementos da matrix:\n',matrix.mean())

# Desvio padrão (standard deviation) dos elementos da matrix
print('Desvio padrão dos elementos da matrix:\n',matrix.std())

