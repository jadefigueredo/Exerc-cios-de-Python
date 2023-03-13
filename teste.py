# Desafio sorteio

# Faça um programa que sorteie um estudante para apresentar um trabalho:

from math import trunc
num = float(input('Digite um valor: ' ))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num, trunc(num)))


import random
n1 = (str(input ('Digite o nome do aluno 1: ')))
n2 = (str(input ('Digite o nome do aluno 2: ')))
n3 = (str(input ('Digite o nome do aluno 3: ')))
n4 = (str(input ('Digite o nome do aluno 4: ')))
li= [n1, n2, n3, n4]
escolhido= random.choice(li)
print('O aluno que irá se apresentar primeiro é {}' .format (escolhido))