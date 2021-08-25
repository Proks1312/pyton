class Cage:
    def __init__(self, num):
        self.num = num

    def operation(self, row):
        return "\n".join(["☢" * row for _ in range(self.num // row)]) + "\n" + "☢" * (self.num % row)

    def __str__(self):
        return f"{self.num}"

    def __add__(self, other):
        print("Результат суммы ячеек:")
        return Cage(self.num + other.num)

    def __sub__(self, other):
        print("Результат вычитания ячеек:")
        return Cage(self.num - other.num) if self.num - other.num >= 0 \
            else "В первой клетке ячеек меньше, чем во второй.Вычитание невозможно"

    def __mul__(self, other):
        print("Результат умножения ячеек:")
        return Cage(self.num * other.num)

    def __floordiv__(self, other):
        print("Результат деления ячеек:")
        return Cage(self.num // other.num)


cage_1 = Cage(55)
cage_2 = Cage(55)
print(cage_1 + cage_2)
print(cage_1 - cage_2)
print(cage_1 * cage_2)
print(cage_1 // cage_2)
print(cage_2.operation(6))
