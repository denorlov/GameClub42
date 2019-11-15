import random

random.seed()
stones = random.randrange(15, 25)
comp_stones_taken = 0
user_stones_taken = 0

print("Перед вами лежит", stones, "камней. Можно брать 1, 2 или 3 камня.")
print("Выигрывает тот, кто забрал последний камень из кучи.")
print("Если ты выиграешь я пропущу тебя дальще. Если проиграешь, то погибнешь")
print()
print("Наша куча:", "* " * stones)

while stones > 0:
    comp_stones_taken = random.randrange(1, 3)
    print("Я беру", comp_stones_taken, "камня")
    stones -= comp_stones_taken
    print("Наша куча:", "* " * stones)

    if stones == 0:
        print("Ха-ха-ха! Я победил")
        break

    print("Сколько ты берешь камней из кучи? Можно взять 1, 2 или 3 камня.")

    user_stones_taken = int(input())
    while user_stones_taken > 3 or user_stones_taken < 1 or stones - user_stones_taken < 0:
        print("Эй, так не по правилам! Попробуй 1, 2 или 3 камня!")
        user_stones_taken = int(input())
    stones = stones - user_stones_taken

    if stones == 0:
        print("Эх, твоя взяла, ты победил!")
        break

    print("Наша куча:", "* " * stones)
