from collections import defaultdict

d = defaultdict(list)
for el in range(1, 3):
    num = input(f'Введите {el} шестнадцатиричное число: ')
    d[el] = list(num)
# d['1'] = ['a', '2']
# d['2'] = ['c', '4', 'f']
print(d)
res = 0
for el in d.values():
    res += int(''.join(el), 16)

summ = list(str(hex(res)))
# print(res)
print(f'Сумма: {summ[2:]}\n'
      f'{"".join(summ[2:])}')

res = 1
for el in d.values():
    res *= int(''.join(el), 16)

mul = list(str(hex(res)))
# print(res)
print(f'Произведение: {mul[2:]}\n'
      f'{"".join(mul[2:])}')