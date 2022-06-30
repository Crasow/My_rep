import os

print('Соревнование по PYTHON')
number = int(input('Сколько участников?'))
members = []

while number != 0:
    members.append(input('Кто на %d месте ?' % number))
    number -= 1
print('В соревновании учавствовали ', members)
print('Поздравим победителей:')
pos = 1
i = 0
while pos <= 3:
    print(pos, 'место занял', members[i])
    pos += 1
    i += 1
print(members)
