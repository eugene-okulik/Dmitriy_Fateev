number = 7

while True:
    guess = int(input("Угадай цифру: "))
    if guess == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
