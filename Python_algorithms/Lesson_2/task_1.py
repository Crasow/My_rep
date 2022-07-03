def calculator():
    user_data = input('Введите через пробел первое число, второе число и знак: ').split()
    fnum, snum, sign = user_data
    fnum, snum = float(fnum), float(snum)
    if sign == '0':
        return 'Finished'
    elif sign == '+':
        res = fnum + snum
        print(res)
        return calculator()
    elif sign == '-':
        res = fnum - snum
        print(res)
        return calculator()
    elif sign == '*':
        res = fnum * snum
        print(res)
        return calculator()
    elif sign == '/':
        if snum == 0:
            print('На ноль делить нельзя')
            return calculator()
        else:
            res = fnum / snum
            print(res)
            return calculator()
    else:
        print('Введен неверный знак, попробуйте еще раз')
        return calculator()


print(calculator())
