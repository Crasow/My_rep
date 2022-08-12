from random import randint


def game():
    print('Отгадай число от 0 до 100, у тебя 10 попыток')
    lifes = 10
    res = randint(0, 100)
    for el in range(lifes):
        user_num = int(input('Твое число:'))
        if user_num > res:
            print('Твое число больше нужного, попробуй еще раз')
            lifes -= 1
        elif user_num < res:
            print('Твое число меньше нужного, попробуй еще раз')
            lifes -= 1
        elif user_num == 'stop':
            return 'bye'
        else:
            print('Поздравляю, ты победил. Сыграем еще раз?')
            return game()

    print('Все попытки исчерпаны. Сыграем еще раз?')
    return game()


print(game())
