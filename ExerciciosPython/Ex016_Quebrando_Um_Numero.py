'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

import math
#from math import trunc

numero = float(input('Digite um numero não inteiro: '))

numeroInteiro = math.trunc(numero)
print('O valor digitado foi {} e a sua porção inteir é {}'.format(numero, numeroInteiro) )