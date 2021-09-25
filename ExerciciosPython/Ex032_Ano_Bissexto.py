'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from datetime import datetime

# datetime object containing current date and time

ano = int (input('Que ano quer analisar? Coloque 0 para analisar o ano atual:  '))


now = datetime.now()
 
print("now =", now)

if now == 0:
    ano = now


if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO0'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO0'.format(ano))

# dd/mm/YY H:M:S
#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)	
