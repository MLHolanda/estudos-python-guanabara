#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Desafio_13:
#Faça um algoritmo que leia o salário 
#de um vendedor e mostre seu novo salário, 
#com 15% de aumento
sal = float(input('Digite o salário atual R$'))
n_sal = sal * 1.15
print(f'O Novo salário é R${n_sal:.2f}')


# Lendo os dados
salario_atual = float(input('Digite o salário atual: R$ '))
porcentagem_aumento = float(input('Qual a porcentagem de aumento? '))

# Calculando o aumento de forma clara
# A fórmula: valor * (porcentagem / 100)
valor_do_aumento = salario_atual * (porcentagem_aumento / 100)
novo_salario = salario_atual + valor_do_aumento

# Exibindo os resultados de forma organizada
print('-' * 30)
print(f'Salário antigo: R$ {salario_atual:>10.2f}')
print(f'Aumento ({porcentagem_aumento}%): R$ {valor_do_aumento:>10.2f}')
print(f'Novo Salário:   R$ {novo_salario:>10.2f}')
print('-' * 30)








# In[ ]:





# In[ ]:



