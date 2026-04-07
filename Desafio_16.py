#• Desafio 016: Crie um programa que leia 
#um número Real qualquer pelo teclado 
# e mostre na tela a sua porção Inteira. 
# (Ex: Digite 6.127, a parte inteira é 6).
'''
import emoji
import math

print(emoji.emojize(':polegar_para_cima:' , language='pt') *10)
nr = float(input('Digite o número: '))
print(emoji.emojize(':polegar_para_cima:' , language='pt') *10)       
'''


#Desafio_16
# Crie um programa que leia um número real pelo teclado e mostre sua porção
# inteira. (Ex:6.127, a parte inteira é 6).
import math
#import emoji
n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, math.trunc(n)))
print(f'O número {n} tem a parte inteira {math.trunc(n)}')