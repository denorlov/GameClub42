from moria.functions import get_answer, end_of_game, happy_end
import pygame

def начало(prev_location):
    print('''   Только под вечер, в пасмурных сумерках, остановились усталые путники на отдых.
Багрово-черная громада Баразинбара дышала вниз холодом - дул порывистый ветер. Гэндальф пустил 
свою термокружку по кругу, и все Хранители сделали по глотку. После ужина они собрались на совет.
    - Сегодня ночью мы отдохнем, - объявил Гэндальф, - штурм перевала дорого дался каждому из нас...
    - А куда мы пойдем потом? - спросил Фродо.
    - У Хранителей есть только две дороги, - ответил Гэндальф, - назад в Раздол или вперед к Огненной горе.''')

    answ = get_answer(["1", "вперед", "2", "назад", "3", "направо"])

    if "вперед" in answ or "1" in answ:
        return "перевал"

    elif 'назад' in answ or '2' in answ:
        return "выход"

    elif 'направо' in answ or '3' in answ:
        return "болото"


def болото(prev_location):
    print(''' Вы пришли к древнему туманному болоту. Над поверхностью стоит пар. 
Где-то далеко слышно, как булькает и капает.''')

    answ = get_answer(["1", "прямо", "2", "назад"])

    if "прям" in answ or "1" in answ:
        if prev_location == "перевал":
            return "начало"
        elif prev_location == "начало":
            return "перевал"

    elif 'назад' in answ or '2' in answ:
        if prev_location == "перевал":
            return "перевал"
        elif prev_location == "начало":
            return "начало"

def перевал(prev_location):
    print(' Вы забрались на перевал. Прямо над вами разверглось небо. Полил дождь, поднялся ветер, \
загромыхали молнии.')

    answ = get_answer(["1", "прямо", "2", "направо", "3", "назад"])

    if "прям" in answ or "1" in answ:
        if prev_location == "дверь":
            return "начало"
        elif prev_location == "начало":
            return "дверь"
        elif prev_location == "болото":
            return "дверь"

    elif "направо" in answ or "2" in answ:
        if prev_location == "дверь":
            return "начало"
        elif prev_location == "начало":
            return "болото"
        elif prev_location == "болото":
            return "дверь"

    elif 'назад' in answ or '3' in answ:
        if prev_location == "дверь":
            return "дверь"
        elif prev_location == "начало":
            return "начало"
        elif prev_location == "болото":
            return "болото"

def дверь(prev_location):
    print('''   Гэндальф опять посмотрел  на Стену. В середине между сторожевыми дубами
она  была  неестественно  гладкой, и Гэндальф, приблизившись к ней вплотную,
начал  ощупывать  ее  руками,  бормоча  какие-то  непонятные  слова.  Потом,
отступив, спросил своих спутников:
    - А теперь? Теперь вы что-нибудь видите?''')

    input("Нажмите enter для продолжения")

    print('''Стену  осветила  взошедшая  луна, но Хранители  не  заметили  никаких изменений - сначала.
А  потом  на  поверхности  Стены  появились   тонкие
серебристые  линии,  стали  постепенно  ярче,  отчетливей, и  вскоре  глазам
изумленных путников открылся искусно выполненный рисунок.
    - Замочная скважина! - воскликнул Гимли, показав на еле заметное углубление в стени.''')

    answ = get_answer(["1", "прямо", "2", "назад"])

    if "прям" in answ or "1" in answ:
        happy_end()

    elif "назад" in answ or "2" in answ:
        return "перевал"


pygame.mixer.init()

pygame.mixer.music.load('in-the-dark.mp3')
pygame.mixer.music.play(-1)

print("\n" * 100)

prev_location = "начало"
location = "начало"
new_location = "начало"

while True:
    print(prev_location, location, new_location)
    if location == "начало":
        new_location = начало(prev_location)
    elif location == "болото":
        new_location = болото(prev_location)
    elif location == "перевал":
        new_location = перевал(prev_location)
    elif location == "дверь":
        new_location = дверь(prev_location)

    if new_location == "выход":
        end_of_game()
        break

    prev_location = location
    location = new_location

