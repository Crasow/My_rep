fnum = int(input('Введите ваше первое число: '))
snum = int(input('Введите ваше второе число: '))
tnum = int(input('Введите ваше третье число: '))

if snum < fnum < tnum or tnum < fnum < snum:
    print(f'Это {fnum}')
elif fnum < snum < tnum or tnum < snum < fnum:
    print(f'Это {snum}')
else:
    print(f'Это {tnum}')
