from random import randint

rand_list = [randint(0, 1000) for el in range(10)]
print(rand_list)


def swap(my_list):
    _min = _max = my_list[0]
    for el in range(len(my_list)):
        if my_list[el] > _max:
            _max = my_list[el]
            i_max = el
        elif my_list[el] < _min:
            _min = my_list[el]
            i_min = el
    my_list[i_min], my_list[i_max] = _max, _min
    return my_list


print(swap(rand_list))
