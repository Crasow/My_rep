user_num = input('Ваше число: ')
even = 0
odd = 0
for el in user_num:
    if int(el) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'{even} четных и {odd} нечетных')
