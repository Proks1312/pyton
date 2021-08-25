class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return "\n".join("\t".join([f'{itm:03}' for itm in line]) for line in self.lists)

    def __add__(self, other):
        try:
            i = [[int(self.lists[line][itm]) + int(other.lists[line][itm]) for itm in range(len(self.lists[line]))]
                 for line in range(len(self.lists))]
            return Matrix(i)
        except IndexError:
            return f"Неправильный размер матрицы"


matrix_a = [[1, 3, 3], [3, 3, 2], [2, 4, 1], [0, 5, 2]]
matrix_b = [[2, 3, 6], [3, 6, 7], [7, 4, 3], [9, 0, 2]]

m_1 = Matrix(matrix_a)
m_2 = Matrix(matrix_b)
amount_m = m_1 + m_2
print(amount_m)
