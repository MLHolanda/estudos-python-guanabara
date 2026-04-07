'''
Desafio_14
Escreva um programa que pergunte a quantidade de KM 
percorridos por um carro alugado, assim com a quantidade
de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que:
A diária do carro custa: R$60,00 / dias
O KM rodado custa: R$0,15.
'''
km = float(input('Quantos KM o carro percorreu? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
diaria = float(input('Qual o valor da diária? R$'))
kr = float(input('Qual o valor do KM rodado? R$'))
valor_total = (km * kr) + (dias * diaria)
print(f'O valor a pagar pelo aluguel é R${valor_total:.2f}')