from string import ascii_lowercase

letter_1 = input('Введите первую букву: ')
letter_2 = input('Введите вторую букву: ')

letters = ascii_lowercase
fnum = 0
snum = 0
for el in letters:
    fnum += 1
    snum += 1
    if el == letter_1:
        print(f'"{el}" {fnum} буква в афавите')
        fnum_stop = fnum
    if el == letter_2:
        print(f'"{el}" {snum} буква в афавите')
        print(f'Между ними {snum - fnum_stop-1} букв')
