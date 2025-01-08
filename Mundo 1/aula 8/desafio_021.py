# este desafio pede para tocar uma música com python.
# tem que ter a música baixada, seu nome de preferência sem acentos ou caracteres especiais.
import pygame
pygame.init()
pygame.mixer.music.load('nome do arquivo de musica')
pygame.mixer.music.play()
pygame.event.wait()