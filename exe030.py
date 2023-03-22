# Desafio 30

# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

numero = int(input('Digite qualquer número inteiro aqui:')) 
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))