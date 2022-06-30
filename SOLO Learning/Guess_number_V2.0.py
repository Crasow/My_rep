import random

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
player__num = int(input())
while life > 0:
    life -= 1
    print('Осталось', life, 'жизней')
    if player__num == target:
        print('Победа!')
        break
    elif player__num > target:
        if life == 0:
            print('Проебано')
            break
        player__num = int(input('Не угадал. Твое число больше.'))
    elif player__num < target:
        if life == 0:
            print('Проебано')
            break
        player__num = int(input('Не угадал. Твое число меньше.'))
else:
    print('Проебано')
