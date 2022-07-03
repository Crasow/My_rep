from time import time
from random import randint
from timer import timer

time_list = []
# nums = [randint(0, 10) for el in range(5)]
nums = [7, 9, 10, 1, 10, 6]


# @timer
def bubble_sort(arr):
    for el in range(len(arr) - 1):
        for ell in range(len(arr) - el - 1):
            if arr[ell] > arr[ell + 1]:
                arr[ell], arr[ell + 1] = arr[ell + 1], arr[ell]
    return arr


print(nums)
print(bubble_sort(nums))
