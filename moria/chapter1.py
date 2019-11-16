import pygame

from moria.functions import end_of_game, get_answer


def chapter1():
    global answ
    print("Вы вышли на мост около Восточных ворот.")
    print("Впереди слышен рык и рев. Земля содрогается.")
    print("Что вы намерене делать? Идти '1. вперед', отступить '2. назад'?")
    pygame.mixer.music.load('arghhh.mp3')
    pygame.mixer.music.play(-1)
    answ = get_answer(["1", "2", "вперед", "назад"])
    if "вперед" in answ or "1" in answ:
        print("Барлог вышел вам навстречу и начал кидать в вас камнями и огенными шарами.")
        end_of_game()

    elif "назад" in answ or "2" in answ:
        print("Вы испугались, развернулись и побежали со всех ног."
              " Барлог вышел вам навстречу и начал кидать в вас камнями и огенными шарами.")
        end_of_game()

