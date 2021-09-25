'''
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para 
o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever 
na tela se o usuário venceu ou perdeu.
'''
import random

computador = random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-'*20)
usuario = int(input('Em que número eu pensei? '))
print('Pensei no número {}'.format(computador))

if usuario == computador:
    print('Não acredito que você adivinhou :(')
else:
    print('Sabia que você não ia acertar, haha :)')