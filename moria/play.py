import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load('sounds/amb_wind_1.flac')
pygame.mixer.music.play(-1)
#pygame.mixer.music.play()

time.sleep(50)

pygame.mixer.music.stop()
