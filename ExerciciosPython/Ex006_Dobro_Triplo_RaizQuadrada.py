'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

numero = float(input('Digite um numero: '))

dobro = numero * 2
print('O dobro de {} é {}'.format(numero,dobro))

triplo = numero * 3
print('O triplo de {} é {}'.format(numero,triplo))


RaizQ = (numero ** (1/2))
print('A raiz quadrada de {} é {}'.format(numero,RaizQ))
