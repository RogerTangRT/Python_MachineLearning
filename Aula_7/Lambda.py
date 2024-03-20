# https://www.youtube.com/watch?v=G3COxzJ1SW0&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=7
# Função Lambda e funções anônimas (Python para machine learning - Aula 7)
# É uma forma resumida do def

def somaQuadrados(a,b):
    somaQ = a**2 + b**2
    return somaQ

print('Soma Quadrados:', somaQuadrados(2,3))

# Função Lambda
somaQuadradosLambda = lambda a,b:a**2 + b**2
print('Soma Quadrados Lambda:', somaQuadradosLambda(2,3))

metade = lambda valor:valor/2
valor = 16
print('Função metade (divide por 2):', 'Valor:',valor, 'Metade',metade(valor))