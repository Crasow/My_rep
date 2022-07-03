class calc:
    def __init__(self, f_num, s_num):
        self.f_num = int(''.join(f_num), 16)
        self.s_num = int(''.join(s_num), 16)

    def __add__(self, other):
        res = list(str(hex(self.f_num + self.s_num)))
        return res[2:]

    def __mul__(self, other):
        res = list(str(hex(self.f_num * self.s_num)))
        return res[2:]


f_num = 'a2'
s_num = 'c4f'
# f_num = input()
# s_num = input()
summ = calc(f_num, s_num) + calc(f_num, s_num)
mul = calc(f_num, s_num) * calc(f_num, s_num)
print(f'Сумма - {summ}\nПроизведение - {mul}')
