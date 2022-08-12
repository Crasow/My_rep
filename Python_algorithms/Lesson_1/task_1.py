user_num = input('Напишите трехзначное число: ')
res = 0
for el in user_num:
    res += int(el)

print(res)
res = 1
for el in user_num:
    res = res * int(el)

print(res)
