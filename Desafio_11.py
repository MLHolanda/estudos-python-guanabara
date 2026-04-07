'''
Desafio_11
Faça um programa que leia a altura e largura de 
uma parede em metros e calcule sua área e a 
quantidade de tinta que será usada para pintá-la.
Sabendo que cada litro de tinta pinta 2 metros quadrados.
'''
alt = float(input('Qual é a altura da parede? '))
larg = float(input('Qual é a largura da parede? '))
area = alt * larg
tin = area / 2
print(f'Temos uma área de {area:.2f} metros e gastaremos {tin:.2f} litros de tinta')
