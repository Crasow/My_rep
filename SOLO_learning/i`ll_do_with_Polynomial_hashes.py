import hashlib
from time import time
from timer import timer
from random import choice

# my_list = [{'apple': 5, 'banana': 12, 'pear': 34, 'kiwi': 2, 'mango': 4}, {'cucmber': 7, 'tomato': 27, 'potato': 42}]
my_str = 'qwertyuioopasdfghjkllzxcvbnm'
my_list = [choice(my_str) for el in range(10000)]

new_str = ''
for el in my_list:
    new_str += el

sublines = set()


# -------------------------------------------
@timer
def casual(line):
    for el in range(len(line)):
        for ell in range(len(line), el, -1):
            sublines.add(line[el:ell])


start = time()
casual(new_str)
# print(time() - start)
print(len(sublines))


# ----------------------------------------------------------
@timer
def new(line):
    dip = (set([line[i:j + i + 1] for i in range(len(line)) for j in range(len(line) + 1)]))
    print(len(dip))


new(new_str)
