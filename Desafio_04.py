''' Desafio_04
Faça um script que leia algo pelo teclado
E mostre seu tipo primitivo
E todas as informações possíveis sobre ele
'''
a = input('Digite algo: ')
print(f'O tipo primitivo de: {a} é ==={type(a)}=== ')
print(f'Só tem espaços? ==={a.isspace()}===')
print(f'É um número? ==={a.isnumeric()}===')
print(f'É alfabético? ==={a.isalpha()}===')
print(f'É alfanumérico? ==={a.isalnum()}===')
print(f'está em maiúsculas? ==={a.isupper()}===')
print(f'Está em minúsculas? ==={a.islower()}===')
print(f'Está capitalizada? ==={a.istitle()}===')
