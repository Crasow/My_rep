my_list = [5, 6, 4, 4, 4, 4, 2, 1, 7, 4, 6, 9]


res = [[0, 0]]
for el in my_list:
    count = 0
    for ell in my_list:
        if ell == el:
            count += 1
        if count > res[0][1]:
            res[0][0] = el
            res[0][1] = count
print(f'Число {res[0][0]} повторяется {res[0][1]} раз')

