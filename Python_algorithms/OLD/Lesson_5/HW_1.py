from collections import namedtuple

dev_count = int(input('Введите количество предприятий: '))
Dev = namedtuple('development', 'name q1 q2 q3 q4')
devs_avg = {}
for el in range(dev_count):
    dev = Dev(
        name=input("Введите название предприятия: "),
        q1=int(input('Введите выручку за 1 квартал: ')),
        q2=int(input('Введите выручку за 2 квартал: ')),
        q3=int(input('Введите выручку за 3 квартал: ')),
        q4=int(input('Введите выручку за 4 квартал: '))
    )
    devs_avg[dev.name] = (dev.q1 + dev.q2 + dev.q3 + dev.q4) / 4
# 14   80
avg = sum(devs_avg.values()) / dev_count

print(f'Средняя годовая прибыль всех предприятий: {avg}')
print(f'Предприятия, с прибылью выше среднего значения:', end=' ')

for k, v in devs_avg.items():
    if v > avg:
        print(k, end=' ')

print(f'\nПредприятия, с прибылью ниже среднего значения:', end=' ')

for k, v in devs_avg.items():
    if v < avg:
        print(k, end=' ')
