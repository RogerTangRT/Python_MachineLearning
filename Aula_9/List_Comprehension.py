# https://www.youtube.com/watch?v=NlRUAq6-meg&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=9
# List Comprehension em Python (curso Python para machine learning - Aula 9)

velocidades_kmph = [40,50,56,64,73,79,85,96,100,120]
print('Velocidade Km/h:', velocidades_kmph)
velocidades_milhasph = []
for velocidade in velocidades_kmph:
    velocidades_milhasph.append(velocidade/1.61)
print('Velocidade Milhas/h:', velocidades_milhasph)

# usando map. aplicar um conjunto de dados a uma função

velocidades_milhasph_map = list(map(lambda x:x/1.61,velocidades_kmph))
print('Velocidade Milhas map/h:', velocidades_milhasph_map)

# List Comprehension
velocidades_milhasph_Comprehension = [x/1.61 for x in velocidades_kmph] 
print('Velocidade Milhas Comprehension/h:', velocidades_milhasph_Comprehension)

caracteres = [i for i in 'Didática Tech']
print('caracteres',caracteres)