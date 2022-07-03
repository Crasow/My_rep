n = int(input('Ваше число: '))
n_str = ''
res = 0
for el in range(n):
    n_str += f'{str(el + 1)} + '
    res += el + 1
print(f'{n_str[:-2]} = {res}')

print(f'n*(n+1)/2 = {int(n * (n + 1) / 2)}')
