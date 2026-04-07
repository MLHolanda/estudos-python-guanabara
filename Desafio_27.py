'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Desafio_27
Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida 
o primeiro e o último nome separadamente.
Ex: Ana maria de Souza
primeiro: Ana
último: Souza

'''
nome = str(input('Digite seu nome completo: ')).strip().split()
print(nome)
print(f'Seu primeiro nome é {nome[0]}, o último nome é {nome[len(nome)-1]} ')
