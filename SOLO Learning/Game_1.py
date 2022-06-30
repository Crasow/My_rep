import random

bank = ['автострада', 'бензин', 'инопланетянин',
        'самолет', 'библиотека', 'шайба', 'олимпиада',
        'коньки', 'хоккей']
secret_word = random.choice(bank)
# print(secret_word)
print("КУ-КУ епта. Я тебе тут слово загадал. У тебя всего 8 попыток его отгдать.")
print("Поехали!")
gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

game = 0
errors_cnt = 0
while game == 0:
    win = 0

    letter = input('Вводи свою букву, черт: ')
    if len(letter) != 1:
        continue
    print('Ты решил что это буква \"' + letter + '\" ?')

    if letter in secret_word:  # hit
        print("Ну ладно, это ты угадал ")
        i = 0
        for symbol in secret_word:
            if symbol == letter:
                gamer_word[i] = letter
            i += 1
    else:  # miss
        errors_cnt += 1
        print("ХА! ЛОХ! \nКол-во лохов: " + str(errors_cnt))
        if errors_cnt == 8:
            print("проиграно")
            break

    for symbol in gamer_word:
        if symbol != '*':
            win += 1
        if win == len(secret_word):
            game = 1
            print('В этот раз ты победил ... мудила ... \nНо не думай что в следующий раз будет так просто!')
    print(''.join(gamer_word))
