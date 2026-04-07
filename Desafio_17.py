4# Desafio_17
# Faça um programa que leia o comprimento do cateto oposto e adjacente
# de um triângulo. Calcule e mostre o comprimento da hipotenusa.

# A fórmula para calcular a hipotenusa (\(a\)) de um triângulo retângulo
# é baseada no Teorema de Pitágoras, expressa por \(a=\sqrt{b^{2}+c^{2}}\\).
# Ela determina que a hipotenusa é a raiz quadrada da soma dos quadrados dos
#catetos (\(b\) e \(c\)).
co = float(input('Digite o CO : '))
ca = float(input('Digite o CA: '))

hi = co**2 + ca**2
hip = hi**(1/2)
print(f'A Hipotenusa {hi} vale: {hip:.2f}')
print('=' * 20)
import math
b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.sqrt(b**2 + c**2) # Abordagem 'rústica' usando a fórmula direta
print('=' * 20)
print('A hipotenusa vai medir {:.2f}'.format(hip))
print('=' * 20)
print(f'A hipotenusa vai medir {hip:.2f}')


# Desafio_17 - Abordagem 'rústica'
# Este é um exemplo separado para demonstrar o cálculo da hipotenusa
# usando a fórmula direta do Teorema de Pitágoras.
#import math
from math import hypot

cateto_oposto_rustic = float(input('Digite o comprimento do cateto oposto para o exemplo rústico: '))
cateto_adjacente_rustic = float(input('Digite o comprimento do cateto adjacente para o exemplo rústico: '))

hipotenusa_rustic = math.hypot(cateto_oposto_rustic, cateto_adjacente_rustic)

print(f'A hipotenusa (abordagem rústica) vai medir {hipotenusa_rustic:.2f}')