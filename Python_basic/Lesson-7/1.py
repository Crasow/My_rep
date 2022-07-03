class Matrix:
    matrix = [[0, 0],
              [0, 0]]

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in Matrix.matrix]))

    def __add__(self):
        for i in range(len(self.list1)):
            for ii in range(len(self.list2[i])):
                Matrix.matrix[i][ii] = self.list1[i][ii] + self.list2[i][ii]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in Matrix.matrix]))


m = Matrix([[4, 34],
            [5, 3]],
           [[4, 23],
            [1, 45, ]])

print(m.list1)
print(m.list2)
print(m.__add__())


