from time import time
from random import randint

time_new = []
time_old = []
nums = [randint(100, 1000) for el in range(1000)]


def fast_select_sort(arr):
    for el in range(len(arr)):
        s_num_id = arr.index(min(arr[el:]), el)
        if s_num_id != el:
            arr[s_num_id], arr[el] = arr[el], arr[s_num_id]
    return arr


def not_enough_fast_select_sort(arr):
    for el in range(len(arr)):
        s_num_id = arr.index(min(arr[el:]), el)
        arr[s_num_id], arr[el] = arr[el], arr[s_num_id]
    return arr


n = 0
while n < 10:
    start = time()
    fast_select_sort(nums.copy())
    stop = time()
    time_new.append(stop - start)

    start = time()
    not_enough_fast_select_sort(nums.copy())
    stop = time()
    time_old.append(stop - start)
    n += 1

new_avg = sum(time_new)/len(time_new)
old_avg = sum(time_old)/len(time_old)
print(time_new)
print(time_old)
print(new_avg, 'fast_select_sort')
print(old_avg,'not_enough_fast_select_sort')