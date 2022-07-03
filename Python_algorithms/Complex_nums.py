class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        self.summx = self.x + obj.x
        self.summy = self.y + obj.y
        return self.summx, self.summy

    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y
        return self.multx, self.multy


x = 2
y = 3
a1 = Complex(x, y)
x = 4
y = 5
a2 = Complex(x, y)
res = a1 + a2
res2 = a1 * a2
print(res, res2)

x = 2
y = 3
a1 = complex(x, y)
x = 4
y = 5
a2 = complex(x, y)
summ = a1 + a2
mult = a1 * a2
print(summ, mult)
