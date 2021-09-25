'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Número {} é Par!'.format(numero))
else:
    print('Número {} é Ímpar!'.format(numero))
