n = int(input('Ваше число: '))
fnum = -0.5
res = 0
for el in range(n):
    res += fnum
    fnum /= -2
print(res)