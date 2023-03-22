# Desafio 31

# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem. Cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância da sua viagem em km?'))
print('Sua viagem terá {}km' .format(distancia))

if distancia <= 200:
    valor = distancia * 0.52
    print('Você irá pagar R${:.2f}' .format(valor))
else:
    valor = distancia * 0.45
    print('Você irá pagar R${:.2f}' .format(valor))