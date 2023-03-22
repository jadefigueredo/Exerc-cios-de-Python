# Desafio 28 - Condições

# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

n = randint(0, 5)

print('Adivinhe qual número eu estou pensando entre 0 e 5. Tente adivinhar...')

jogador = (int(input('Em que número eu pensei? ')))

if jogador == n:
    print(int(input('PARABÉNS, VOCÊ ACERTOU!')))
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(n, jogador)) 


