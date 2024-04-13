import random
from decouple import config
import configparser
from win_or_lose_logic import determine_win_or_loss

# Считываем начальный капитал из файла settings.ini
config_parser = configparser.ConfigParser()
config_parser.read('settings.ini')
initial_money = int(config_parser['Settings']['MY_MONEY'])

# Список чисел от 1 до 10
numbers = list(range(1, 11))

def play_game():
    money = initial_money

    while True:
        print(f"Ваш текущий капитал: ${money}")
        bet = int(input("Сделайте ставку на число от 1 до 10: $"))

        if bet > money:
            print("У вас недостаточно средств для совершения ставки.")
            continue

        chosen_number = int(input("Выберите число от 1 до 10: "))

        if chosen_number not in numbers:
            print("Некорректное число. Пожалуйста, выберите число от 1 до 10.")
            continue

        winning_number = random.choice(numbers)
        print(f"Выпало число: {winning_number}")

        result = determine_win_or_loss(bet, chosen_number, winning_number)

        if result == "win":
            print("Поздравляем! Вы выиграли!")
            money += bet * 2
        else:
            print("К сожалению, вы проиграли.")
            money -= bet

        play_again = input("Хотите ли вы сыграть еще? (да/нет): ")
        if play_again.lower() != 'да':
            break

    print(f"Игра завершена. Ваш итоговый капитал: ${money}")

    print('До свидания!')

if __name__ == "__main__":
    play_game()