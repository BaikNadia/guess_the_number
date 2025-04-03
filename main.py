import random

def guess_number():
    """
    Игра 'Угадай число'. Компьютер загадывает число от 1 до 100,
    а игрок пытается его угадать.
    """
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте его угадать!\n")

    # Компьютер загадывает случайное число
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Запрос числа у пользователя
        try:
            guess = int(input("Введите ваше число: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        # Считаем количество попыток
        attempts += 1

        # Проверяем угаданное число
        if guess < secret_number:
            print("Загаданное число больше вашего.\n")
        elif guess > secret_number:
            print("Загаданное число меньше вашего.\n")
        else:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
            break

# Запускаем игру
if __name__ == "__main__":
    guess_number()
    
