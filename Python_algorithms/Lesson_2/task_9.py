user_nums = input('Введите числа через пробел: ').split()
the_biggest = 0
for el in user_nums:
    sum = 0
    for ell in el:
        sum += int(ell)
    if the_biggest < sum:
        the_biggest = sum
print(the_biggest)
