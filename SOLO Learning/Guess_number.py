import random

target = random.randint(0, 100)
player__num = int(input('Введи число'))
print(target)
while player__num != target:
    if player__num > target:
        player__num = int(input('Введи число меньше'))
    elif player__num < target:
        player__num = int(input('Введи число больше'))
print('Победа!')
answer = input('Хочешь перейти на 2 уровень?(y/n)')
if answer == 'n':
    print('Ну ладно(')
else:
    player__num = int(input('Введи число. Только учти: теперь у тебя 8 жизней\n'))
    target = random.randint(0, 100)
    print(target)
    life = 7
    while True:
        if life == 0:
            print('Проебано')
            break
        elif player__num > target:
            player__num = int(input('Введи число меньше'))
        elif player__num < target:
            player__num = int(input('Введи число больше'))
        else:
            print('Победа!')
            break
        life -= 1
