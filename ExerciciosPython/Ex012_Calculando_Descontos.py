'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

PrecoProduto = float (input('Digite o preço do produto em R$: '))

Desconto = (PrecoProduto * 5)/100

PrecoComDesconto = PrecoProduto - Desconto

print('O preço do produto é {:.2f} com 5% '.format(PrecoProduto) +'desconto será: {:.2f}'.format(PrecoComDesconto))