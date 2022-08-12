import random

game = int(input('Играть одному - 1\nИграть coop - 2\n'))
if game == 1:
    target = random.randint(1, 100)
    # print(target)
    levels = {1: 10, 2: 8, 3: 5, 4: 3, 5: 1}
    print('Какой уровень сложности выберешь?')
    for part in levels:
        print('На', part, 'уровне сложности', levels[part], 'жизней')
    level = int(input())
    life = levels[level]
    while level > 5:
        level = int(input('Такого нет, выбери другой\n'))
    print('Хорошо. Теперь введи свое первое число.\nТолько учти: теперь у тебя', life, 'жизней')
    gamer_num = int(input())
    while life > 0:
        life -= 1
        print('Осталось', life, 'жизней')
        if gamer_num == target:
            print('Победа!')
            break
        elif gamer_num > target:
            if life == 0:
                print('Ты проиграл')
                break
            gamer_num = int(input('Не угадал. Твое число больше.'))
        elif gamer_num < target:
            if life == 0:
                print('Ты проиграл')
                break
            gamer_num = int(input('Не угадал. Твое число меньше.'))
    else:
        print('Ты проиграл')
if game == 2:
    gamer_count = int(input('Сколько игроков: \n'))
    gamers = []
    # Ввод имен
    for gamer in range(gamer_count):
        gamer_name = input(f'Введите имя игрока {gamer + 1}: ')
        gamers.append(gamer_name)

    target = random.randint(1, 100)
    # print(f'---------{target}---------')
    gamer_num = None
    levels = {1: 10, 2: 8, 3: 5, 4: 3, 5: 1}
    print('Какой уровень сложности выберете?')
    for part in levels:
        print('На', part, 'уровне сложности', levels[part], 'жизней')
    level = int(input())

    while level > 5:
        level = int(input('Такого нет, выберите другой\n'))

    life = levels[level]

    print(f'У вас по {life} жизней')

    while target != gamer_num:
        # проверка на луз
        if life == 0:
            print('Ваши жизни кончились(((')
            break
        else:
            print(f'Осталось {life} жизней')
            # счет жизней
        life -= 1
        # начало цикла по очереди
        for gamer in gamers:

            gamer_num = int(input(f'{gamer}, введи свое число: '))

            if gamer_num > target:
                print(f'{gamer}, ты не угадал. Твое число больше нужного.')
            elif gamer_num < target:
                print(f'{gamer}, ты не угадал. Твое число меньше нужного.')
            else:  # очень странно реализованное условие победы))
                print(f'Поздравляю, {gamer},', end=' ')
                break
    else:
        print(f'ты победил!')
