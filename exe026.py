# Desafio 26

# Crie um programa que leia uma frase e mostre quantas vezes aparece a letra "A", qual a posição em que ela aparece a primeira vez e qual posição aparece a última vez.

frase = str(input('Digite uma frase: ')).lower().strip()
print( 'A letra "a" aparece {} vezes na sua frase.'.format(frase.count('a')))
print('A primeira letra "a" apareceu na posição {}' .format(frase.find('a')+1))
print('A última letra "a" apareceu na posição {}' .format(frase.rfind('a')+1))