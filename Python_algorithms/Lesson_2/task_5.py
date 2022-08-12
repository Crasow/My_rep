my_dict = {}
start = 32
for el in range(127 - 32):
    my_dict[chr(start)] = start
    start += 1

count = 0
for k, v in my_dict.items():
    count += 1
    print(f'"{k}" -  {v}', end=', ')
    if count % 10 == 0:
        print('')
