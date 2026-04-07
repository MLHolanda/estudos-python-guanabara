'''O enunciado do Exercício 022 do curso de Python 
do Gustavo Guanabara (Analisador de Textos) é o 
seguinte:
Crie um programa que leia o nome completo 
de uma pessoa e mostre:" [1, 2] 

* O nome com todas as letras maiúsculas;
* O nome com todas as letras minúsculas;
* Quantas letras ao todo (sem considerar espaços);
* Quantas letras tem o primeiro nome. [1, 2] 

Dicas para a resolução:

* Você precisará usar métodos de manipulação de strings como .upper(), .lower(), .strip() e .count().
* Para contar o primeiro nome, você pode usar o método .find() para localizar o primeiro espaço ou transformar o nome em uma lista com .split(). [1, 2] 
'''
#Lendo o nome e removendo os espaços em branco, no #inicio e fim com (strip())
nome = str(input('Digite seu nome completo: \n\n')).strip()# Tira os espaços vazios antes e depois do nome

print(f'\nAnalisando seu nome...\n')
# 1. Nome em maiúsculas
print(f'Seu nome em maiúsculas é: {nome.upper()}\n')
# 2. Nome em minúsculas
print(f'Seu nome em minúsculas é: {nome.lower()}\n')
primeiro = nome.split()

# 3. Quantas letras ao todo (sem contar espaços)
# Pegamos o tamanho total (len() e subtraímos os espaços em branco nome.count(' ')
print(f'Seu nome tem ao todo {len(nome)} letras, conntando os espaços\n')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras, sem espaços\n')
print(f'Tem {nome.count(" ")} espaços em branco\n')
# Uma forma prátuica de encontrar onde está o primeiro espaço
print(f'Seu primeiro tem {nome.find(" ")} letras\n')

print(f'Seu primeiro tem {nome.rfind(" ")} letras\n')

print(f'Seu primeiro nome é {primeiro[0]} e ele tem {nome.find(" ")} letras\n')
#primeiro_nome = nome.split()
print(f'Seu primeiro nome é {primeiro[0]} e ele tem {len(primeiro[0])} letras\n')

