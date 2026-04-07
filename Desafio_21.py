'''
Desafio_21
"Faça um programa em Python que abra e reproduza o 
áudio de um arquivo MP3." 

'''
import pygame
import time
#pygame.init() #Gustavo aqui
#inicializa o sistema de som 
pygame.mixer.init()

#carrega a sua musica
pygame.mixer.music.load('musica.mp3')

#começa a tocar
print('Prepare os ouvidos....tocando musica.mp3!')
pygame.mixer.music.play()
#pygame.event.wait() #Gustavo aqui
#no linux, precisamos deste comando para o python esperar a música tocar
# Ele vay tocar por 10 segundos e depois parar

time.sleep(10)
print('Teste finalizado')
