import random

print('Загадай число от 1 до 100, а компьтер будет угадывать')
print('Используй подсказки в виде "<" если число меньше загаданного и ">" если число больше загаданного ')
gamer_num = int(input('Введи свое число: '))
comp_num = random.randint(0, 100)
gap = [0, 100]
i = 0
average = 0
while True:
    # Первый этап с рандомом
    # print(gap)
    if i == 0:
        print(comp_num)
        if comp_num == gamer_num:
            print('Комп угадал!')
            break
        tip = input('Введи подсказку\n')
        if tip != '<' or tip != '>':
            print('SkyNet уже выехал')
            continue
        elif tip == '<':
            if comp_num > gamer_num:
                print('Ну и чё ты сделал?')
                continue
            if comp_num > gap[0]:
                gap[0] = comp_num + 1
        elif tip == '>':
            if comp_num < gamer_num:
                print('Ну и чё ты сделал?')
            if comp_num < gap[1]:
                gap[1] = comp_num - 1
    # Второй этап с average
    if i >= 1:
        print(int(average))
        if average == gamer_num:
            print('Комп угадал!')
            break
        tip = input('Введи подсказку\n')
        if tip == '<':
            if comp_num > gamer_num:
                print('Ну и чё ты сделал?')
                continue
            if average > gap[0]:
                gap[0] = average + 1
        elif tip == '>':
            if comp_num < gamer_num:
                print('Ну и чё ты сделал?')
                continue
            if average < gap[1]:
                gap[1] = average - 1
    average = int((int(gap[0]) + int(gap[1])) / 2)
    # i += 1
