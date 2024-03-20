# https://www.youtube.com/watch?v=OPJnTuBwySY&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=2
# Listas em Python (curso Python para machine learning - Aula 2)
a = [1,2,3]
print(a)
a.append(15)
print(a)

b = [7,8,9]
# a.append(b)
# print(b)
# Resultado = [7, 8, 9]

for indice in range(0, len(b)):
    a.append(b[indice])
print(a)

a = [1,2,3]

for elemento in b:
    a.append(elemento)
print(a)