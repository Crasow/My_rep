from memory_profiler import profile
from memory_profiler import memory_usage
from random import randint


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_used = m2[0] - m1[0]
        return res, mem_used

    return wrapper


"""
Скрипт №1
"""


# Решение из примера к дз
@decor
def eratosfen(i):
    # O(n log(log n))
    """Используя алгоритм «Решето Эратосфена»"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


# Улучшенный вариант примера
@decor
def eratosfen_2(i):
    # O(n log(log n))
    """Используя алгоритм «Решето Эратосфена»"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    yield [p for p in sieve if p != 0][i - 1]


# my_generator, mem_diff = eratosfen(100)  # 0.19140625 Mib
# print(f"Выполнение 1 заняло {mem_diff} Mib")
# my_generator, mem_diff = eratosfen_2(100)  # 0.00390625
# print(f"Выполнение 2 заняло {mem_diff} Mib")
"""
Вывод: в первом варианте скрипта есть инкремент в +-0.5 Mib, но замена
"return" на "yield" достаточно исправляет ситуацию.
"""

"""
Скрипт №2
"""


# Рекурсивный метод
@profile
def g_progression_recur():
    user_qty = 500

    def recur(n_qty, qty, res=0, num=1):
        if qty >= 1:
            return recur(n_qty, qty - 1, res + num, num / -2)
        else:
            print(f'Количество элементов: {n_qty}, их сумма {res}')

    return recur(user_qty, user_qty)


# g_progression_recur()  # Инкремент +- 1


# Метод без рекурсии
@profile
def g_progression():
    user_qty = 500
    num = 1
    res = 1
    for el in range(user_qty - 1):
        num = num / -2
        res += num
    print(f'Количество элементов: {user_qty}, их сумма {res}')


# g_progression() # Инкремент незначителен

"""
Вывод: рекурсия во время выполнения хранит стек и требует для этого
память, что вполне поправимо обычной итерацией
"""

"""
Скрипт №3
"""


# До
@profile
def my_func():
    list1 = [randint(0, 1000000) for el in range(100000)]
    list2 = [el for num, el in enumerate(list1) if list1[num - 1] < list1[num]]
    print(f'Исходный список {list1}')
    print(f'Новый список {list2}')


# После
@profile
def my_func_2():
    list1 = [randint(0, 1000000) for el in range(100000)]
    list2 = [el for num, el in enumerate(list1) if list1[num - 1] < list1[num]]
    print(f'Исходный список {list1}')
    del list1
    print(f'Новый список {list2}')


my_func()
my_func_2()
"""
Итог: Хранение большого количества данных в списке вызвало инкремент
4.6 MiB. После получения нужных данных в list2, list 1 уже не нужен и его 
спокойно можно удалить и осводить 1.6 MiB
"""
