'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

#from random import choice
import random

aluno01 = input('Nome do primeiro aluno: ')
aluno02 = input('Nome do segundo aluno: ')
aluno03 = input('Nome do terceiro aluno: ')
aluno04 = input('Nome do quarto aluno: ')

lista = [aluno01, aluno02, aluno03, aluno04]

escolha = random.choice(lista)

print('O aluno escolhido foi {}'.format(escolha))