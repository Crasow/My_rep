def bin(n, base):
    str = '0123456789ABCDF'
    if n < base:
        return str[n]
    else:
        return bin(n // base, base) + str[n % base]


print(bin(23, 2))


def bin2(n, base):
    str = '0123456789ABCDF'
    result = ''
    while n >= base:
        b = n % base
        n = n // base
        result = result + str[b]
    else:
        result = result + str[n]
    return result


a = list(reversed(bin2(23, 2)))
for el in a:
    print(f'{el}', end='')
# print(bin2(10, 2))
