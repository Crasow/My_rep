class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __str__(self):
        return f' Результат операции {self.qty * "*"}'

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        return self.qty - other.qty if (self.qty - other.qty) > 0 else print('Отрицательное кол-во клеток')

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __truediv__(self, other):
        return Cell(round(self.qty // other.qty))

    def make_order(self, qty_in_row):
        result = ''
        row = '*' * qty_in_row
        row_qty = range(self.qty // qty_in_row)
        for i in row_qty:
            result += f'{row}\n'
        result += f'{"*" * (self.qty % qty_in_row)}'
        return result


cell1 = Cell(11)
cell2 = Cell(6)
print(cell1)
print(cell1 + cell2)
print(cell1.make_order(5))
print(cell2.make_order(5))
print(cell1 / cell2)
