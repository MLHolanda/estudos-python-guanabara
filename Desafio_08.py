'''Desafio_08: Measurement Converter (Conversor de Medidas)
value_meters = float(input('Enter value in meters: '))
Calculations (Multiplicamos para descer na escala)
'''
value_meters = float(input('Digite o valor em metros: '))
km = value_meters / 1000
hec = value_meters / 100
dam = value_meters / 10
met = value_meters
dec = value_meters * 10    # decimeters (decímetros)
cent = value_meters * 100   # centimeters (centímetros)
mili = value_meters * 1000  # millimeters (milímetros)

# Output (Saída traduzida)
print(f'The value {value_meters}m corresponds to:')
print(f'{km}km, \n{hec}hec, \n{dam}dam, \n{met}met, \n{dec}dm, \n{cent}cm \nand {mili}mm')


#Desafio_08:
#Escreva um programa que leia um valor 
#em metros e o exiba convertido 
#em centímetros e milímetros 

val = float(input('Valor em metros: '))
km = val / 1000
hec = val / 100
dam = val / 10
met = val
dec = val * 10
cent = dec* 10
mil =  cent * 10

print(f'A nedida é {val} , \nem kilometros vale {km} , \nem hectometros vale {hec} , \nem decametros vale {dam} , \nem metros vale {met} , \nem decimetros vale {dec} , \nem centimtros vale: {cent} \ne em milimetros vale: {mil} ')

