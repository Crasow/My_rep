def minimal():
    my_list = [5, -6, 4, 4, 4, -4, 2, 1, -7, 4, 6, -9]
    count = 0
    for el in my_list:
        if el < 0:
            count += 1
    if count < 0:
        return 'Нет отрицательных чисел'
    _min = min(my_list)
    return _min


print(minimal())
