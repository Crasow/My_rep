from random import randint

m = 3
array = [randint(1, 10) for el in range(2 * m + 1)]


# array = [1, 1, 3, 4, 4, 9, 10]

def finder(arr):
    # ----------------

    # -----------------

    for el in arr:
        a = 0
        b = 0
        x = -1
        for z in arr:
            if z == el:
                x = x + 1
        for ell in arr:
            if el > ell:
                a += 1
            if el < ell:
                b += 1
        if a > b:
            b = b + x
        else:
            a = a + x
        if a == b:
            return el


def surrender(arr):
    arr = sorted(arr)
    return arr[int(len(arr) / 2)]


print(surrender(array), 'Правильный ответ')
print(finder(array), 'Надеюсь, правильный ответ')
print(sorted(array), 'Отсортированный список')
