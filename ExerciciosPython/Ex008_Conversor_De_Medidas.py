'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

numero = float(input('Digite um numero em metros: '))

km = numero/1000
print('\nPara convertermos de m para quilômetro, dividimos por 1000')
print('{} m em km é {} km'.format(numero, km))

hm = numero/100
print('\nPara convertermos de m para hectômetro, dividimos por 100')
print('{} m em hm é {} km'.format(numero, hm))


dm = numero/10
print('\nPara convertermos de m para decâmetro, dividimos por 10')
print('{} m em dm é {} dam'.format(numero, dm))

print('\nO valor em metros é {} m'.format(numero))

dcm = numero*10
print('\nPara convertermos de m para decímetro, multiplicamos por 10')
print('{} m em dcm é {} dm'.format(numero, dcm))

cm = numero*100
print('\nPara convertermos de m para centímetro, multiplicamos por 100')
print('{} m em cm é {} cm'.format(numero, cm))

mm = numero*1000
print('\nPara convertermos de m para milímetro, multiplicamos por 1000')
print('{} m em mm é {} mm'.format(numero, mm))
print('\n')