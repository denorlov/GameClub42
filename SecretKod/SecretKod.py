import random

random.seed()
num = random.randrange(1, 9999)
# print(num)
max_attempts_count = 10

print("Чтобы войти в подземелье мории, отгдай секретный шифр. Это число от 0000 до 9999. "
      "У тебя есть", max_attempts_count, "попыток!")

user_num = int(input("Введите код (число от 0000 до 9999):"))
attempt = 1

while user_num != num and attempt < max_attempts_count:
      digit1 = num % 10
      digit2 = ((num - digit1) // 10) % 10
      digit3 = ((num - digit2 * 10 - digit1) // 100) % 10
      digit4 = ((num - digit3 * 100 - digit2 * 10 - digit1) // 1000) % 10

      user_digit1 = user_num % 10
      user_digit2 = ((user_num - user_digit1) // 10) % 10
      user_digit3 = ((user_num - user_digit2 * 10 - user_digit1) // 100) % 10
      user_digit4 = ((user_num - user_digit3 * 100 - user_digit2 * 10 - user_digit1) // 1000) % 10

      # print(digit4, digit3, digit2, digit1)
      # print(user_digit4, user_digit3, user_digit2, user_digit1)

      match_value_and_position = 0
      match_value = 0

      if user_digit1 == digit1:
            digit1 = -1
            match_value_and_position += 1

      if user_digit2 == digit2:
            digit2 = -1
            match_value_and_position += 1

      if user_digit3 == digit3:
            digit3 = -1
            match_value_and_position += 1

      if user_digit4 == digit4:
            digit4 = -1
            match_value_and_position += 1


      if user_digit1 == digit2:
            digit2 = -1
            match_value += 1
      elif user_digit1 == digit3:
            digit3 = -1
            match_value += 1
      elif user_digit1 == digit4:
            digit4 = -1
            match_value += 1

      if user_digit2 == digit1:
            digit1 = -1
            match_value += 1
      elif user_digit2 == digit3:
            digit3 = -1
            match_value += 1
      elif user_digit2 == digit4:
            digit4 = -1
            match_value += 1

      if user_digit3 == digit1:
            digit1 = -1
            match_value += 1
      elif user_digit3 == digit2:
            digit2 = -1
            match_value += 1
      elif user_digit3 == digit4:
            digit4 = -1
            match_value += 1

      if user_digit4 == digit1 or user_digit4 == digit2 or user_digit4 == digit3:
            match_value += 1

      # print(digit4, digit3, digit2, digit1)
      # print(user_digit4, user_digit3, user_digit2, user_digit1)

      print("Для кода:", user_digit4, user_digit3, user_digit2, user_digit1)
      print("цифр совпадающих по позиции и значению:", match_value_and_position, end=", ")
      print("только по значению: ", match_value)

      attempt += 1
      print("Попытка", attempt, "из", max_attempts_count, "введите код (число от 0000 до 9999):")
      user_num = int(input())

if user_num == num:
      print("Вы отгадали код, проходите!")

elif attempt >= max_attempts_count:
      print("Количество ваших попыток истекло")
      print("Я загадал", num)
