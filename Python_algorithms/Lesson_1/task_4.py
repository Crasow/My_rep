import random
import string


val1 = input('Введите нижнюю границу целого числа: ')
val2 = input('Введите верхнюю границу целого числа: ')
print(random.randint(int(val1), int(val2)))

val1 = input('Введите нижнюю границу вещественного числа: ')
val2 = input('Введите верхнюю вещественного целого числа: ')
print(str(random.uniform(float(val1), float(val2)))[:5])


count_v1, count_v2 = 0, 0
val1 = input('Введите границу от начала алфавита: ')
val2 = input('Введите границу от конца алфавита: ')
for el in string.ascii_lowercase:
    if el == val1:
        val1 = count_v1
    else:
        count_v1 += 1
    if el == val2:
        val2 = count_v2
    else:
        count_v2 += 1

confines = string.ascii_lowercase[val1:val2]
print(random.choice(confines))
