# Desafio 22: 

# 1) O nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas;

nome = str(input('Digite seu nome completo: '))

print('Seu nome em maiúsculas é {}'.format(nome.upper()))

# 2) O nome completo de uma pessoa e mostre o nome com todas as letras minúsculas;

print('Seu nome em minúsculas é {}' .format(nome.lower()))

# 3) O nome completo de uma pessoa e mostre quantas letras ao todo (sem considerar espaços);

# Verifica o espaçamento entre as letras vai ser o comprimento do nome menos a quantidade de espaços.

print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))

# 4) Quantas letras tem o primeiro nome;

print ('Seu primeiro nome tem {} letras' .format(nome.find(' ')))