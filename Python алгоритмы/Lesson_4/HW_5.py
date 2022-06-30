from timeit import timeit


# user_num = 3


def simple_def(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple is True:
            if count == i:
                break
            count += 1
        n += 1
    return n


def sieve(serial_num, arr=[2]):
    counter = 2
    num = 2
    while counter <= serial_num:
        is_simple = True
        for simple in arr:
            if num % simple == 0:
                is_simple = False
        if is_simple:
            arr.append(num)
            counter += 1
        num += 1

    return f'Простое число с порядковым номером {serial_num} : {arr[-1]} '


def sieve_2(serial_num, arr=[2]):
    counter = 2

# """
# 2
# """
# user_num = 2
# print(timeit('simple_def(user_num)', globals=globals(), number=1000), '1')  # 0.0006154000000000021 1
# print(timeit('sieve(user_num)', globals=globals(), number=1000), '2')  # 0.0006536000000000007 2
# """
# 10
# """
# user_num = 10
# print(timeit('simple_def(user_num)', globals=globals(), number=100), '1')  # 0.0015223000000000007 1
# print(timeit('sieve(user_num)', globals=globals(), number=100), '2')  # 7.7344904 2
# """
# 100
# """
user_num = 100
# print(timeit('simple_def(user_num)', globals=globals(), number=10), '1')  # 0.0015647000000003075 1
# print(timeit('sieve(user_num)', globals=globals(), number=10), '2')  # 0.27592259999999946 2

from cProfile import run

run('sieve(user_num)')
