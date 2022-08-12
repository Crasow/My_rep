from time import time

my_list = [el for el in range(100000000)]
lowest_nums = []


def fync_1(start_list, fin_list):
    while len(fin_list) < 2:
        _min = start_list[0]
        for el in start_list:
            if el < _min:
                _min = el
        fin_list.append(_min)
        start_list.remove(_min)

    return f'Два наименьших числа: {fin_list[0]}, {fin_list[1]}'


start = time()
print(fync_1(my_list, lowest_nums))  # Время выполнения 4.148905277252197
stop = time()
print(f'Время выполнения {stop - start}')

my_list = [el for el in range(100000000)]

lowest_nums = []


def fync_2(start_list, fin_list):
    if len(fin_list) == 2:
        return f'Два наименьших числа: {fin_list[0]}, {fin_list[1]}'
    else:
        _min = start_list[0]
        for el in start_list:
            if el < _min:
                _min = el
        fin_list.append(_min)
        start_list.remove(_min)
        return fync_2(start_list, fin_list)


start = time()

print(fync_2(my_list, lowest_nums))  # Время выполнения 4.151897430419922
stop = time()
print(f'Время выполнения {stop - start}')
"""
Как и ожидалось, метод с рекурсией тратит больше времени на решение задачи (в среднем на 1-2 секунды),
чем классический цикл.
Хотя оба метода имеют сложность O(n)
"""
