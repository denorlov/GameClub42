import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load('in-the-dark.mp3')
pygame.mixer.music.play(-1)
#pygame.mixer.music.play()

time.sleep(50)

pygame.mixer.music.stop()
