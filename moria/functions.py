import pygame

def end_of_game():
    print("Вы погибли. Нажмите enter для продолжения")
    pygame.mixer.music.load('end-cut.mp3')
    pygame.mixer.music.play()
    input()
    print("\n" * 100)


def happy_end():
    print("Поздравляю, ты победил!")
    pygame.mixer.music.load('happy-end.mp3')
    pygame.mixer.music.play()
    print("Нажмите enter для продолжения")
    input()
    print("\n" * 100)


def get_answer(variants):
    answer = ""
    while answer not in variants:
        print("Не понятно, что вы хотите сделать. Введите правильную команду.")
        answer = input("Ваш выбор?").strip().lower()
    return answer
