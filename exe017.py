# Desafio 17

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# É possível solucionar essa atividade de duas formas:

# Forma 1: O quadrado da hipotenusa é igual a soma do quadrado dos catetos, logo, a hipotenusa é a raiz quadrada da soma do quadrado dos catetos.

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# Forma 2: Importando a classe math, é possível calcular a hipotenusa e obter a resposta do exercício.

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}' .format (hi))