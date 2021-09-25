'''
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

numero = float(input('Digite um numero: '))

#Antecessor
ant = numero - 1

#Sucessor 
suc = numero + 1

print('O antecessor e o sucessor de {} são {} e {}, respectivamente'.format(numero, ant,suc))