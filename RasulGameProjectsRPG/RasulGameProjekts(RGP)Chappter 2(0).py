import pygame
import time


pygame.mixer.init()
pygame.mixer.music.load('05.mp3')
pygame.mixer.music.play(-1)
time.sleep(1)
print('                                  Квест:Рыцарь Дня .Глава 2 "Погоня к Ученому"')
a = input('Введите имя')
print('Поздравляю', a, '. Ты выбрался из базы возьми мотоцыкл если у тебя нет и двигайся в лабораторию имени Альчика ')
print('Там тебя ждет Алексей Моргенштерн ученый 100 ранга и глава совета О5 он тебе даст объект'
      ' SCP-058-ES((Бесконечня батарейка))')
print('Никаим образом не дай получть Др.Стасу этот объект Удачи тебе агент')
print('Ты едешь по дороге к лаборатории и в тебя начинают шмалять это агенты Др.Стаса .Они простреливают колесо '
      'твоего мотцикла, тебяже отбрасывает в сторону , но ты ещё можешь размышлять и кое как двигаться ')
print("Твои действия ")
print("(1)Подойти к ближайщему укрытию")
print("(2)Попробовать переждать гнет пуль")
print("(3)Попробовать уйти до ближайшей станции метро ((До станции 20 метров))")
print("(4)Попробовать переубедить их стрелять")
c = input()
if c == '1':
    print('Ты попытался подойти к укрытиию но один из снайперов тебя подстрелили (You Died)')
    pygame.mixer.music.load('Roblox-death-sound.mp3')
    pygame.mixer.music.play(-1)
    time.sleep(1)
if c == '2':
    print('Кто начал стрелять с твоей стороны и убивать агентов Др.Стаса он подеъзжает к тебе берет себе на руки кладет')
    print('на свой мотоцикл и уезжает в Лабароторию . Вы подъезжаете к лаборатории и ты заснул ')
    print('Ты очнулся в лаборатории((К тебе подходит тот байкер который тебя спас)).')
    print('Спросить у нее вопросы')
    print('(1)Кто ты такой ?(2)Как ты меня спасла ?(3)Ты предатель чи не ?(4)Ученый здесь ?')
    b = input()
    if b == '1':
        print('Я тоже агент как и ты ,но я ((Снимает шлем байкера)) женшина.Привет', a, '.Меня зовут '
                                                                                        '"Макарина мать сочная милфа" ')
        print('(2)Как ты меня спасла ?(3)Ты предатель чи не ?(4)Ученый здесь ?')
        b = input()
    if b == '2':
        print('На мой телефон Xiaomi пришло уведомление о том что надо спати тебя от агентов Др.Стаса . Ну я пришла '
              'и смотрю что в тебя стреляют ну я их и застрелила.ЛОЛ')
        print('(1)Кто ты такой ?(3)Ты предатель чи не ?(4)Ученый здесь ?')
        b = input()
    if b == '3':
        print('Я не придатель . Моя гланая задача тебя доставить до ученого.')
        print('(1)Кто ты такой ?(2)Как ты меня спасла ?(4)Ученый здесь ?')
        b = input()
    if b == '4':
        print('К сожалению ученый ушел он на половине пути от сюда что бы нам к ним подъехать нужно чудо.')
        print(a, ':Я знаю одного человека по имени Расул и он сможет на помочь')
        print('Ну что ждем выезжаем к нему.')
        pygame.mixer.music.load('2-hours-later-spongebob.mp3')
        pygame.mixer.music.play(1)
        time.sleep(3)
        print('Вот и он наконец мы его нашли')
        print('"Макарина мать сочная милфа": И это он как то странно он выглядит')
        print(a, ':Он может так выглядить ,но он очень силен')
        print('"Макарина мать сочная милфа":Ты издеваешся он же жирный как он нам поможет ?')
        print(a, ':Увидешь')
        print('((Вы подошли к нему))О Расул привет.')
        print('О привет', a,'как жизнь ,как сам.')
        print('Да все нормально спасибо.')
        print('Расул:По тебе так нескажешь .Я зачемто был нужен ?')
        print(a, ':Да.Помнишь какую я тебе услугу преподнес?')
        print('Расул:Как я мог забыть кончно помню.Если бы не ты меня даже здесь бы неболо')
        print("Позади вас началась стрельба это снова были агенты Др.Стаса ((Странно как они вас все время находят))")
        print("Ваши возможности")
        print('(1)Спрятатся за укрытие и отсреливаться')
        print('(2)Протсто отстреливаться')
        d = input()
        if d == '1':
            print('Вы спряталиь за укрытие, но расул произнес фразу "ZA WARUDO"')
            pygame.mixer.music.load('za-warudo-stop-time-sound.mp3')
            pygame.mixer.music.play(-1)
            time.sleep(5)
            print('И все агенты Др.Стаса умерли в один миг')
            print('"Макарина мать сочная милфа":Что это черт побери было?')
            print(a, ':Это была его способность "ZA WARUDO" эта способность останавливает все моллекулы во всм мире а '
                     'свои моллекулы делает быстрее.')
            print('"Макарина мать сочная милфа":А для тупых ')
            print(a, ':Замедляет время')
            print('Расул:Вам что нужно ')
            print(a, ':Посмотрел на "Макарина мать сочная милфа" и сказал')
            print('(1)ДА(2)НЕТ')
            g = input()
            if g == '1':
                print('Расул:Ладно')
                print('TO BE CONTINUED...............')
                pygame.mixer.music.load('TO BE CONTINUED.mp3')
                pygame.mixer.music.play(-1)
                time.sleep(12)
            if g == '2':
                print('Расул:Ну я все понял ')
                print('TO BE CONTINUED...............')
                pygame.mixer.music.load('TO BE CONTINUED.mp3')
                pygame.mixer.music.play(-1)
                time.sleep(12)
        if d == '2':
            print('Вы начали отстреливаться , но расул произнес фразу "ZA WARUDO"')
            pygame.mixer.music.load('za-warudo-stop-time-sound.mp3')
            pygame.mixer.music.play(-1)
            time.sleep(5)
            print('И все агенты Др.Стаса умерли в один миг')
            print('"Макарина мать сочная милфа":Что это черт побери было?')
            print(a, ':Это была его способность "ZA WARUDO" эта способность останавливает все моллекулы во всм мире а '
                     'свои моллекулы делает быстрее.')
            print('"Макарина мать сочная милфа":А для тупых ')
            print(a, ':Замедляет время')
            print('Расул:Вам что нужно ')
            print(a, ':Посмотрел на "Макарина мать сочная милфа" и сказал Да')
if c == '3':
    print('Ты пытаешься кое-как уклонятся от пуль но снайпер "Макарина мать сочная милфа" вас подстрелила(You Died)')
    pygame.mixer.music.load('Roblox-death-sound.mp3')
    pygame.mixer.music.play(-1)
    time.sleep(1)
if c == '4':
    print('Ты поднял руки вверх чтобы они в тебя не стреляли,ты ели ели поднялся на ноги и сказал что сдаешся.И тут по '
          'твоему затулку кто то ударил и упал ты бессознпния и вас взяли в заложники')
    print('TO BE CONTINUED...............')
    pygame.mixer.music.load('TO BE CONTINUED.mp3')
    pygame.mixer.music.play(-1)
    time.sleep(12)