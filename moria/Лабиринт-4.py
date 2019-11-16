from moria.chapter1 import chapter1
from moria.chapter2 import chapter2
from moria.chapter3 import chapter3
from moria.functions import get_answer, end_of_game, happy_end
import pygame

print("\n" * 100)
pygame.mixer.init()

while True:
    pygame.mixer.music.load('in-the-dark.mp3')
    pygame.mixer.music.play(-1)

    print("Вы находитесь в центральном зале подземелья Мории.")
    print("Вы можете пойти '1. прямо', '2. влево' или '3. вправо'.")

    answ = get_answer(["1", "2", "3", "прям", "влево", "вправо"])

    if "прям" in answ or "1" in answ:
        chapter1()

    elif 'влево' in answ or '2' in answ:
        chapter2()

    elif 'вправо' in answ or '3' in answ:
        chapter3()
