import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load('05.mp3')
pygame.mixer.music.play(-1)
time.sleep(50)
pygame.mixer.muisc.stop()