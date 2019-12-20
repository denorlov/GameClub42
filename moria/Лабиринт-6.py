from moria.functions import get_answer, end_of_game, happy_end
import pygame

pygame.mixer.init()

print("\n" * 100)

prev_location = "начало"
location = "начало"
next_location = "начало"

key_found = False
poison_found = False

print(''' Только под вечер, в пасмурных сумерках, остановились усталые путники на отдых. 
Багрово-черная громада Баразинбара дышала вниз холодом - дул порывистый ветер. 
Гэндальф пустил свою термокружку по кругу, и все Хранители сделали по глотку. 
После ужина они собрались на совет.
- Сегодня ночью мы отдохнем, - объявил Гэндальф...
- А куда мы пойдем потом? - спросил Фродо.
- У Хранителей есть только две дороги, - ответил Гэндальф, - назад в Раздол или вперед к Огненной горе.''')

while True:
    print()
    print("debug>>", " prev_location=", prev_location, ", location=", location, sep="")
    print()

    if location == "начало":
        pygame.mixer.music.load('sounds/in-the-dark.mp3')
        pygame.mixer.music.play(-1)

        print('''Вы в самом начале долгого пути''')

        answ = get_answer(["1", "вперед", "2", "назад", "3", "направо"])

        if "вперед" in answ or "1" in answ:
            next_location = "перевал"

        elif 'назад' in answ or '2' in answ:
            next_location = "выход"

        elif 'направо' in answ or '3' in answ:
            next_location = "болото"

    elif location == "болото":
        pygame.mixer.music.load('sounds/atmosbasement.mp3_.flac')
        pygame.mixer.music.play(-1)

        print(''' Вы пришли к древнему туманному болоту. Над поверхностью стоит пар. Где-то далеко слышно, как булькает и капает.''')

        answ = get_answer(["1", "прямо", "2", "назад"])

        if "прям" in answ or "1" in answ:
            if prev_location == "перевал":
                next_location = "начало"
            elif prev_location == "начало":
                next_location = "перевал"

        elif 'назад' in answ or '2' in answ:
            if prev_location == "перевал":
                next_location = "перевал"
            elif prev_location == "начало":
                next_location = "начало"

    elif location == "перевал":
        pygame.mixer.music.load('sounds/storm_3_siren.mp3')
        pygame.mixer.music.play(-1)

        print(''' Вы забрались на перевал. Прямо над вами разверглось небо. Полил дождь, поднялся ветер, загромыхали молнии.''')

        answ = get_answer(["1", "прямо", "2", "направо", "3", "назад"])

        if "прям" in answ or "1" in answ:
            if prev_location == "дверь":
                next_location = "начало"
            elif prev_location == "начало":
                next_location = "дверь"
            elif prev_location == "болото":
                next_location = "дверь"

        elif "направо" in answ or "2" in answ:
            if prev_location == "дверь":
                next_location = "начало"
            elif prev_location == "начало":
                next_location = "болото"
            elif prev_location == "болото":
                next_location = "дверь"

        elif 'назад' in answ or '3' in answ:
            if prev_location == "дверь":
                next_location = "дверь"
            elif prev_location == "начало":
                next_location = "начало"
            elif prev_location == "болото":
                next_location = "болото"

    elif location == "дверь":
        pygame.mixer.music.load('sounds/rock_breaking.flac')
        pygame.mixer.music.play()

        print(''' Гэндальф опять посмотрел  на Стену. В середине между сторожевыми дубами она была неестественно гладкой,
и Гэндальф, приблизившись к ней вплотную, начал  ощупывать  ее  руками,  бормоча  какие-то непонятные слова.
Потом, отступив, спросил своих спутников:
- А теперь? Теперь вы что-нибудь видите?''')

        print('''Стену осветила  взошедшая  луна, но Хранители  не  заметили  никаких изменений - сначала.
А потом на поверхности cтены появились тонкие серебристые  линии, стали постепенно ярче, 
отчетливей, и  вскоре глазам изумленных путников открылся искусно выполненный рисунок.
- Замочная скважина! - воскликнул Гимли, показав на еле заметное углубление в стени.''')

        answ = get_answer(["1", "прямо", "2", "назад"])

        if "прям" in answ or "1" in answ:
            happy_end()

        elif "назад" in answ or "2" in answ:
            next_location = "перевал"


    if next_location == "выход":
        end_of_game()
        break

    prev_location = location
    location = next_location