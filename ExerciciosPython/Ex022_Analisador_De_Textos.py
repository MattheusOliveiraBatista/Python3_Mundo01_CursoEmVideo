'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.

'''

texto = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(texto.upper()))
print('Seu nome em minúsculas é {} '.format(texto.lower()))
print('Seu nome tem ao todo {} letras'.format(len(texto) - texto.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(texto.find(' ')))
separa = texto.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))
