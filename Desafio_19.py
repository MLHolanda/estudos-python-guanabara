'''
Exercício 19: Sorteando um item na lista
Enunciado: Um professor quer sortear um dos seus 
quatro alunos para apagar o quadro. Faça um programa 
que ajude ele, lendo o nome deles e escrevendo o 
nome do escolhido.
(Dica: Utilize a biblioteca random).
'''
import random

# Entrada de dados
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')

# Estrutura de Dados: Lista
student = [n1, n2, n3, n4]

# Sorteio
drawn = random.choice(student)

# Saída
print(f'Os candidatos eram: {student}')
print(f'O aluno escolhido foi: {drawn}')