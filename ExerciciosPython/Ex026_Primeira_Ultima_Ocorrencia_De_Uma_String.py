'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()
print('A letra A aprece {} vezes'.format(frase.count('A')))
print('A primeira letra A apreceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apreceu na posição {}'.format(frase.rfind('A')+1))