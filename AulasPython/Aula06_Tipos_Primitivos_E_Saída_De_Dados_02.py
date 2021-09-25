'''
Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). 
Além disso, veremos como fazer as primeiras operações com a função print() do Python.
'''

#n = float(input('Digite um valor'))
n = input('Digite um valor: ')

print(n.isnumeric()) #Verifica se é numperico ou se é possivel converter para o tipo numérico

print(n.isalpha()) #Verifica se a string é alfabético

print(n.isalnum()) #Verifica se é alfanumérico

print(n.islower()) #Verifica se está em minusculos
 