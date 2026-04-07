'''Exercício 18: Seno, Cosseno e Tangente
Enunciado: Faça um programa que leia um ângulo 
qualquer e mostre na tela o valor do seno, cosseno 
e tangente desse ângulo.
(Dica: Pesquise sobre a biblioteca math e a conversão 
de graus para radianos).

Operação,Função em Python,O que ela faz
Converter p/ Radiano,math.radians(angulo),
Transforma graus em radianos.
Seno,math.sin(radiano),Calcula o seno do valor.
Cosseno,math.cos(radiano),Calcula o cosseno do valor.
Tangente,math.tan(radiano),Calcula a tangente do valor.

'''
import math
ângulo = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem seno de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem cosseno de {:.2f}'.format(ângulo, cosseno))
tang = math.tan(math.radians(ângulo))
print('O ângulo da {} tem tangente de {:.2f}'.format(ângulo, tang))
print('=' *30)
# Entrada de dados
angle = float(input('Digite o ângulo que você deseja: '))
# Conversão
radian = math.radians(angle)
# Cálculos
sine = math.sin(radian)
cosine = math.cos(radian)
tangent = math.tan(radian)
# Saída organizada e formatada
print(f'O ângulo de {angle:.1f}° tem:')
print(f'-> SENO: {sine:.2f}')
print(f'-> COSSENO: {cosine:.2f}')
print(f'-> TANGENTE: {tangent:.2f}')
