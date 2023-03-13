# Desafio 27

# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome, separadamente.

n = str(input('Digite seu nome: ')).lower().strip()

nome = n.split()

print('Seu primeiro nome é {}' .format (nome[0]))

# o len faz a busca pela variável nome após o fatiamento, o -1 diminui 1 da frase porque a posição da primeira palavra da frase é sempre 0.

print('Seu último nome é {}' .format(nome[len(nome)-1]))