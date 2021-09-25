'''
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
import random

aluno01 = input('Nome do primeiro aluno: ')
aluno02 = input('Nome do segundo aluno: ')
aluno03 = input('Nome do terceiro aluno: ')
aluno04 = input('Nome do quarto aluno: ')

lista = [aluno01, aluno02, aluno03, aluno04]
escolha = random.shuffle(lista)

print('A ordem de apresentação será ')
print(lista)