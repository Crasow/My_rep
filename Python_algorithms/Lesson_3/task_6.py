def func():
    my_list = [5, 6, 99, 5, 4, 66, 2, 1, 7, 4, 6, 9]
    print(my_list)
    _max = my_list[0]
    _min = my_list[0]
    res = 0
    pack = [0, 0]
    for el in range(len(my_list)):
        if my_list[el] > _max:
            _max = my_list[el]
            pack[0] = el
        if my_list[el] < _min:
            _min = my_list[el]
            pack[1] = el
    pack.sort()
    print(pack)
    for el in range(pack[0] + 1, pack[1]):
        res += my_list[el]
    return res


print(func())
