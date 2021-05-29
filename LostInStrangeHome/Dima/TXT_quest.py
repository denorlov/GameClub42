name = None
health = 10
currentRoom = 'Зал'
inventory = []

rooms = {
    'Зал': {
        'description': "Все здесь, конечно, странно обставленно. Паутина, старое скрипучее кресло-"
                       "качалка. Еще здесь много-много пыли. И как это путник, тебя сюда занесло?\n"
                       "В центре комнаты расположен огромный стол, на столе расставлены огромные,"
                       " если не сказать гигансткие приборы. И еще кто-то собирался ужинать"
                       " при свечах. На столе, на всех предметах мебели расставлены канделябры"
                       " и свечи в канделябрах горят.",
        'юг': 'Кухня',
        'запад': 'Коридор',
    },

    'Кухня': {
        'description': "На кухне на плите стоит пара кастрюл. И в одной из кастрюль что-то жарится!"
                       " Вонь стоит ужасная. Кто, интересно, может есть такую тухлятину?!",
        'север': 'Зал',
        'item': ['monster', 'отмычка']
    },

    'Коридор': {
        'description': "Длинный коридор по которому можно идти вечность. "
                       "Идешь, идешь, идешь, идешь. И все никак не придешь.",
        'восток': 'Зал',
        'юг': 'Сад',
        'север': 'Спальня',
        'item': ['ключ']
    },

    'Сад': {
        'description': "В саду тихо, лишь слега шумит листва на ветру. И еще  немного жутко.",
        'север': 'Коридор'
    },

    'Туалет': {
        'description': "Туалет, как туалет. Унитаз, как унитаз."
                       " Постойте, постойте, банки и склянки какие-то."
                       " Попробуем понюхать, что в них?",
        'запад': "Спальня",
        'item': ['топор лесника']
    },

    'Спальня': {
        'description': "Большая скрипучая двуспальная кровать во всю комнату. И больше ни-че-го!",
        'юг': "Коридор",
        'восток': "Туалет"
    }

}

# ask the player his/her name
if name is None:
    name = input("Как тебя зовут, странник? ")

    print('''
Ваша задача попасть в Сад имея на руках Ключ и Топором лесника.
Да, забыл сказать. Не попадайся монстрам! 
И еще. Каждый раз, когда ты перемещаешься в другую комнату, 
ты устаешь и твое здоровье уменьшается на 1.

Команды:
  идти [направление] (направление может быть: север, юг, восток, запад) 
  взять [предмет]''')

while True:
    print('---------------------------')
    print(name + ' находится в ' + currentRoom)
    print("Здоровье: " + str(health) + ". В рюкзаке: " + str(inventory))

    if "description" in rooms[currentRoom]:
        print(rooms[currentRoom]['description'])

    if "item" in rooms[currentRoom] and not 'monster' in rooms[currentRoom]['item'] and \
            rooms[currentRoom]['item']:
        print('Кажется, здесь есть ' + str(rooms[currentRoom]['item']))
        
    if 'item' in rooms[currentRoom] and \
            'monster' in rooms[currentRoom]['item'] and \
            not 'топор лесника' in inventory:
        print('Ты повстречался с монстром... Конец игры!')
        break

    if health == 0:
        print('У тебя совсем не осталось сил... Ты умер!')
        break

    if currentRoom == 'Сад' and 'ключ' in inventory and 'топор лесника' in inventory:
        print('Тебе удалось выбраться из этого жуткого дома... Ты победил!')
        break

    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split()

    command = move[0]

    if command == 'идти':
        direction = move[1]
        if direction in rooms[currentRoom]:
            if currentRoom == 'Спальня' and\
                    direction == 'восток' and\
                    not 'ключ' in inventory:
                print('Чтобы пройти в дверь из Спальни на запад нужен ключ!')
                continue
            if currentRoom == "Коридор" and direction == 'юг' and\
                    not 'отмычка' in inventory:
                print('Чтобы пройти в дверь из Коридора на юг нужен отмычка!')
                continue

            health = health - 1
            currentRoom = rooms[currentRoom][direction]
        else:
            print('В направлении ' + direction + ' пройти нельзя!')

    if command == 'взять':
        item = move[1]
        if 'item' in rooms[currentRoom] and item in rooms[currentRoom]['item']:
            inventory += [item]
            print(item + ' у нас в кармане!')
            rooms[currentRoom]['item'].remove(item)
        else:
            print('Что такое ' + item + '? Что-то не понимаю, что ты от меня хочешь')