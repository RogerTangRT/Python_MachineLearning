# https://www.youtube.com/watch?v=RhtsCbKyYoA&list=PLyqOvdQmGdTR46HUxDA6Ymv4DGsIjvTQ-&index=25
# Aulão Python sobre Classes, Objetos, Métodos, Herança, Construtor - Aula 25

# Função simples
def teste(v,i):
    valor = v
    incremento = i
    resultado = valor + incremento
    return resultado

a = teste(10,1)

print('\nResultado:',a)

# Criando Classe
class CIncremento:
    def incrementa(self, v,i):
        valor = v
        incremento = i
        resultado = valor + incremento
        return resultado

# instanciando a classe
a = CIncremento()
b = a.incrementa(10,1)
print('\nResultado classe:',b)
print('Chamando e instanciando:' , CIncremento().incrementa(11,1))

# Criando Classe com propriedade
class CIncremento2:
    def incrementa(self, v,i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado

Inc2 = CIncremento2()

print('Chamando e instanciando Incremento 2:' ,Inc2.incrementa(11,1) )
print('Mostrando propriedades')
print('Valor', Inc2.valor)
print('incremento', Inc2.incremento)
print('resultado', Inc2.resultado)

