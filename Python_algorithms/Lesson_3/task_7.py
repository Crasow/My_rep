my_list = [5, 6, 99, 5, 4, 66, 2, 5, 7, 4, 6, 9]
res = []
while len(res) < 2:
    _min = my_list[0]
    for el in my_list:
        if el < _min:
            _min = el
    res.append(_min)
    my_list.remove(_min)

for el in res:
    print(f'{el}', end=' ')
