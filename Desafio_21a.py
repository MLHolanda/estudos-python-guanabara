'''
Desafio_21a
'''
import pygame
import time
#inicializa o sistema de som 
pygame.mixer.init()
#carrega a sua musica
pygame.mixer.music.load('musica.mp3')

#começa a tocar
pygame.mixer.music.play()

#Enquanto a música estiver tocando (busy = ocupado)
while pygame.mixer.music.get_busy():
    time.sleep(1) #O python "espera" 1 segundo e checa novamente
    print('A música continua tocando...')

print('A música acabou e o programa encerrou sozinho!')
