'''
Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
import math

CO = int(input('Digite o cateto oposto: '))
CA = int(input('Digite o cateto adjacente: '))

Hipotenusa = math.hypot(CO,CA)

print('A hipotenusa do triângulo de catetos {} e {} é {}'.format(CO,CA,Hipotenusa))

Ht = math.sqrt((CA*CA)+ (CO*CO))
print('A hipotenusa do triângulo de catetos {} e {} é {}'.format(CO,CA,Ht))
