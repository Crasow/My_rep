from time import time

my_num = 10000


def not_eratosfen_method(num):
    _counter = 1
    _var = 2
    _is_simple = False
    if num == 1:
        return 2
    while _counter != num:
        _var += 1
        for el in range(2, _var):
            if _var % el != 0:
                _is_simple = True
            else:
                _is_simple = False
                break
        if _is_simple:
            _counter += 1
    return _var


start = time()
print(f'Метод без решета {not_eratosfen_method(my_num)}')
stop = time()
print(f'Время выполнения без решета {stop - start}')


def eratosfen_method(num, arr=[2]):
    _counter = 1
    var = 3
    while _counter != num:
        _is_simple = True
        for el in arr:
            if var % el == 0:
                _is_simple = False
                break
        if _is_simple:
            arr.append(var)
            _counter += 1
        var += 1
    else:
        return arr[-1]


start = time()
print(f'Метод с решетом Эратосфена {eratosfen_method(my_num)}')
stop = time()
print(f'Время выполнения с реетом {stop - start}')
"""
Метод без решета Эратосфена имеет сложность O(n^2)
Метод с решетом Эратосфена имеет сложность O(n)
"""