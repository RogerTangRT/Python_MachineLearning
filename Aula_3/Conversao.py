# https://www.youtube.com/watch?v=90Z4p1B4M08&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=3
# Transformando listas float em int (Python para machine learning - Aula 3)
num = 8
print(num)
print('Tipo do numero',type(num))
print(float(num))
print('Tipo do numero com cast(float)',type(float(num)))
print(num)
num = float(num)
print(num)

x = [2,4,10,6]
y = []
for item in x:
    y.append(float(item))
print(y)