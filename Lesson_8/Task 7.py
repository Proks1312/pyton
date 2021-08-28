class ComplexNumber:
    def __init__(self, k, i, *args):
        self.k = k
        self.i = i
        self.l = 'a + b * d'

    def __add__(self, other):
        print(f'Сумма переменных l1 и l2 равна')
        return f'l = {self.k + other.k} + {self.i + other.i} * d'

    def __mul__(self, other):
        print(f'Произведение переменных l1 и l2 равно')
        return f'l = {self.k * other.k - (self.i * other.i)} + {self.i * other.k} * d'

    def __str__(self):
        return f'l = {self.k} + {self.i} * d'


l_1 = ComplexNumber(4, -2)
l_2 = ComplexNumber(2, 2)
print(l_1)
print(l_1 + l_2)
print(l_1 * l_2)