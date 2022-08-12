from memory_profiler import profile


@profile
def wrapper(*args, **kwargs):
    def recur(num):
        if num < 2:
            lst = [el for el in range(40000)]
            return recur(num + 1)

    return recur(*args, **kwargs)


wrapper(0)
