class Cloth:
    def __init__(self, W, H):
        self.W = W
        self.H = H

    def square_coat(self):
        return round(self.W / 6.5 + 0.5)

    def square_jacket(self):
        return round(self.H * 2 + 0.3)

    @property
    def result_square(self):
        return str(f'Общая площадь ткани для пошива: \n'
                   f' {round(self.W / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, W, H):
        super().__init__(W, H)
        self.square_c = round(self.W / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани для пальто {self.square_c} м кв. '


class Jacket(Cloth):
    def __init__(self, W, H):
        super().__init__(W, H)
        self.square_j = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани для костюма {self.square_j} м кв.'


coat = Coat(2, 4)
suit = Jacket(1, 2)
print(coat)
print(suit)
print(coat.result_square)
print(suit.result_square)
print(suit.square_coat())
print(suit.square_jacket())
