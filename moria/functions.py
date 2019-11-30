import pygame

def end_of_game():
    print("Счастливо оставаться, не забудьте выключиться свет перед тем как лечь в кровать. Конец.")
    pygame.mixer.music.load('end-cut.mp3')
    pygame.mixer.music.play()
    input()
    print("\n" * 100)


def happy_end():
    print("Счастливый конец первой части! До новых встречь!")
    pygame.mixer.music.load('happy-end.mp3')
    pygame.mixer.music.play()
    print("Нажмите enter для продолжения")
    input()
    print("\n" * 100)

def get_answer(variants):
    print("Вы можете пойти ", variants)
    answer = input("Ваш выбор?").strip().lower()
    while answer not in variants:
        print("Не понятно, что вы хотите сделать. Введите правильную команду.")
        answer = input("Ваш выбор?").strip().lower()
    return answer
