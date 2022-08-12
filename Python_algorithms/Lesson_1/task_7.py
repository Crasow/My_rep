a = int(input('Первая сторона: '))
b = int(input('Вторая сторона: '))
c = int(input('Третья сторона: '))

if a + b > c and a + c > b and c + b > a:
    print('Такой треугольник существует')
    if a == b and b == c and c == a:
        print('Он еще и равносторонний')
    elif a == b or b == c or c == a:
        print('Он еще и равнобедренный')
    else:
        print('Он еще и разносторонний')
else:
    print('Такого треугольника не существует')
