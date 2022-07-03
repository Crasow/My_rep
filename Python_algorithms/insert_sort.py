from random import randint


def insert_sort(lst):
    for el in range(len(lst)):
        idx = el
        idx_value = lst[el]
        # val = lst[idx-1]

        while (lst[idx - 1] > idx_value) and (idx > 0):
            lst[idx] = lst[idx - 1]
            idx = idx - 1
        lst[idx] = idx_value
        print(lst)
    return lst


my_list = [randint(0, 20) for el in range(10)]

print(insert_sort(my_list))
