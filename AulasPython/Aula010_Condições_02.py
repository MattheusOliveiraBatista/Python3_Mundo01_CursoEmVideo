'''
Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.
'''
nome = str(input('Qual é o seu nome? '))

if nome == 'Matheus':
    print('Seu nome é lindo!')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}!'.format(nome))