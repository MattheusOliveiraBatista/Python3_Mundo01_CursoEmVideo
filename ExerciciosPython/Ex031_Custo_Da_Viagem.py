'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

KmViagem = float(input('Qual é a distância da sua viagem? '))

if KmViagem <= 200:
    print('\nVocê está prestes a começar uma viagemd de {}'.format(KmViagem))
    print('O preço da viagem será de R${:.2f}'.format(KmViagem*0.50))
else:
    print('\nVocê está prestes a começar uma viagemd de {}'.format(KmViagem))
    print('O preço da viagem será de R${:.2f}'.format(KmViagem*0.45))


# Outra forma de fazer

#preço = KmViagem * 0.50 if KmViagem <= 200 else KmViagem * 0.45