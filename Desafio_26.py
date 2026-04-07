'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Desafio_26
Faça um programa que leia uma frase pelo teclado 
e mostre
1 Quantas vezes aparece a letra "A".
2 Em que posição ela aparece a primeira vez.
3 Em que posição ela aparece a última vez.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
frase = str(input('Digite a frase desjada: ')).lower()
print(f'A letra A aparece {frase.count("a")} vezes na frase {frase}:')
print(f'Ela aparece na posição {frase.find("a")+1} primeiro e na posoição {frase.rfind("a")+1} por ultimo')


