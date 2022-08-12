from string import ascii_lowercase

letters = ascii_lowercase
user_num = input('Введите число: ')

count = 0
for el in letters:
    count += 1
    if count == int(user_num):
        print(f'Буква под этим номером: {el}')
