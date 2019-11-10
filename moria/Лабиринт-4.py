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

print("\n" * 100)
pygame.mixer.init()

while True:
    pygame.mixer.music.load('in-the-dark.mp3')
    pygame.mixer.music.play(-1)

    print("Вы находитесь в центральном зале подземелья Мории.")
    print("Вы можете пойти '1. прямо', '2. влево' или '3. вправо'.")

    answ = get_answer(["1", "2", "3", "прям", "влево", "вправо"])

    if "прям" in answ or "1" in answ:
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

        else:
            print("Не понятно, что вы хотите сделать. До свидания.")

    elif 'влево' in answ or '2' in answ:
        print("Вы вышли в левый корридор. Прошли по нему и попали в большой темный зал "
              "с подземным озером в центре. Что-то хлюпает у вас под ногами. "
              "Поздравляю, вас засосала опасная трясина")
        end_of_game()

    elif 'вправо' in answ or '3' in answ:
        print("Вы вышли в правый корридор. Прошли по нему и попали в большой темный зал "
              "с каменным столом в центре. На столе лежит обветшалая книга.")
        print("Это дневник Дурина, в нем он описал осадцу и падения Кхазад-Дум темнымми силами. "
              "Поздравляю, вы нашли настоящее сокровище, экземпляр романской письменности IXIIX века.")
        print("Теперь, с этой рукописью, вы богаты!")

        happy_end()
