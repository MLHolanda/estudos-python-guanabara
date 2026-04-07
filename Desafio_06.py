'''Desafio_06:
#Crie um algoritmo que leia um número e 
#mostre o seu dobro, triplo e raiz quadrada 
'''
n = float(input('Digite um número: '))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)
print('O dobro de {} vale {}'.format(n, n1))
print('O triplo de {} vale {}. A raiz de {} é {:.2}' .format(n, (n*3), n, pow(n, (1/2))))
print(f'O nún é {n} , seu dobro é {n1}, seu triplo é {n2} \ne sua raiz quadrada é {n3} ')
print(f'O dobro é {n*2}.\nO triplo é {n*3}.\nA Raiz é {n**(1/2)}')
