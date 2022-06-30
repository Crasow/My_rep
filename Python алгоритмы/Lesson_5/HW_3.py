from collections import deque
from timeit import timeit


def list_right():
    my_list = [el for el in range(900)]
    return my_list


def deque_right():
    my_deque = deque([el for el in range(900)])
    return my_deque


def list_left():
    my_list = []
    for el in range(900):
        my_list.insert(0, el)
    return my_list


def deque_left():
    my_deque = deque([])
    for el in range(900):
        my_deque.appendleft(el)
    return my_deque


def list_popleft(my_list):
    for el in range(len(my_list)):
        var = my_list[0]
        del my_list[0]
    return var, my_list


def deque_popleft(my_deque):
    for el in range(len(my_deque)):
        var = my_deque.popleft()
    return var, my_deque

# def  list_extendleft():


print(timeit('list_right()', globals=globals(), number=100000))  # 2.0993329
print(timeit('deque_right()', globals=globals(), number=100000))  # 2.5977105999999996
print(timeit('list_left()', globals=globals(), number=100000))  # 27.541488200000003
print(timeit('deque_left()', globals=globals(), number=100000))  # 5.0738761
a = list_left()
b = deque_left()
print(timeit(f'list_popleft({a})', globals=globals(), number=100000))  # 10.504809600000002
print(timeit(f'deque_popleft({b})', globals=globals(), number=100000))  # 4.510460800000004
