'''
print('\033[4;31;43mOlá, Mundo!\033[m') #Underline, letra vermelha e fundo amarelo
print('\033[4;30;45mOlá, Mundo!\033[m') #Underline, letra branca  e fundo magenta
print('\033[7;30mOlá, Mundo!\033[m')#Fundo branco e letra preta - inversão

'''

a = 3
b = 5
nome = 'Matheus'
print('Os valore são \033[32m{}\033[m e \033[31m{}\033[m'.format(a,b ))
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco': '\033[7;30m'

}
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))