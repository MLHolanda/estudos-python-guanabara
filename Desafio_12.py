'''
Desafio_12
Faça um programa que leia o valor
de um produto e retorne seu novo
preço com 5% de desconto.
'''
vp = float(input('Digite o valolr do Produto: R$'))
nv = vp - vp * 5 /100
print(f'O valor que era de R${vp:.2f}, passou para R${nv:.2f} após aplicação do desconto!')
