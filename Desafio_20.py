'''
Exercício 20: Sorteando uma ordem na lista
Enunciado: O mesmo professor do desafio anterior quer 
sortear a ordem de apresentação de trabalhos dos 
alunos. Faça um programa que leia o nome dos quatro 
alunos e mostre a ordem sorteada.
'''
import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

# Dica: usei "lista_alunos" porque "list" é u
# ma palavra reservada do Python
lista_alunos = [n1, n2, n3, n4]

# O comando mágico para embaralhar a lista original:
random.shuffle(lista_alunos)

print('-' * 20)
print('A ordem de apresentação será:')
print(lista_alunos)