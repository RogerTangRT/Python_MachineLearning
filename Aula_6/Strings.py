# https://www.youtube.com/watch?v=AbnPVxoTlqw&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=6
# Manipulando strings com Python (curso Python para machine learning - Aula 6)

frase = 'Estou gostando do curso'
print(frase)

print('Posição 2:',frase[2])
# Pega da 2 a 5 
print('Posição 2 até a 6 frase[2:6]:',frase[2:6])
# Pega da 2 a 7 
print('Posição 2 até a 8 frase[2:8]:',frase[2:8])
# Pega da 5 até o final
print('Posição 5 até o final frase[5:]:',frase[5:])
# Pega da início até a posição 13
print('Posição início até a 13 frase[:13]:',frase[:13])
# Pega da início até a posição 13 pulando de 2 em 2 (passo)
print('Posição início até a 13 pulando de 2 em 2 frase[:13:2]:',frase[:13:2])

# Conta ocorrencia de Letra
print('Count (t):',frase.count('t'))

# Tamanho do string
print('len:',len(frase))

# Replace
frase = frase.replace(' ','.')
print('Alterado:',frase)
