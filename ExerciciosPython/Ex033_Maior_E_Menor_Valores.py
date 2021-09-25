'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
from typing import TextIO


PrimeiroValor = int(input('Digite o Primeiro Valor: '))
SegundoValor = int(input('Digite o Segundo Valor: '))
TerceiroValor = int(input('Digite o Terceiro Valor: '))

menor = PrimeiroValor
maior = PrimeiroValor

if SegundoValor < PrimeiroValor and SegundoValor < TerceiroValor:
    menor = SegundoValor

if TerceiroValor < PrimeiroValor and TerceiroValor < SegundoValor:
    menor = TerceiroValor


print('O menor valor digitado foi {}'.format(menor))

maior = PrimeiroValor

if SegundoValor > PrimeiroValor and SegundoValor > TerceiroValor:
    maior = SegundoValor

if TerceiroValor > PrimeiroValor and TerceiroValor > SegundoValor:
    maior = TerceiroValor

print('O maior valor digitado foi {}'.format(maior))