'''
Desafio_24
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com nome "SANTO",'''

cidade = str(input('Digite o nome da cidade: ')).strip()# Tira os espaços no inicio e no fim do nome
print(cidade[:5].upper() == 'SANTO')
