user_str = input('Ваша строка: ')
user_num = input('Какое число посчитать? ')

count = 0

for el in user_str:
    if el == user_num:
        count += 1
print(f'Число {user_num} встречется {count} раз')
