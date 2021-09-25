'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

from pygame import mixer

mixer.init() 
mixer.music.load('hey.mp3')

mixer.music.play()

parar = input('Digite algo para parar a música...')