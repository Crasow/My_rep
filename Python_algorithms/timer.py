from time import time


def timer(func):
    def wrapper(*args):
        start = time()
        res = func(*args)
        stop = time()
        print(f'Время выполнения {stop - start}')
        return res

    return wrapper
