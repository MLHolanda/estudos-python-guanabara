'''
Desafio_10
Crie um programa que leia quanto 
dinheiro a pessoa tem na sua carteira
e mostre quantos dolares
ela pode comprar
Obs: Considere USS 1,00 = R$3,27
'''
val = float(input('Quanto você tem na carteira? R$'))
dol = val / 3.27

print(f'Com {val:.2f} Você compra US${dol:.2f}')
