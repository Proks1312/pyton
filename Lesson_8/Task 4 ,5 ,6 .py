class Warehouse:
    def __init__(self, name, price, amount, lists_num, *args):
        self.name = name
        self.price = price
        self.amount = amount
        self.lists_num = lists_num
        self.my_warehouse_full = []
        self.my_warehouse = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.amount}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.amount}'

    def receiving(self):
        try:
            unit = input(f'Введите название ')
            unit_1 = int(input(f'Введите цену за ед '))
            unit_2 = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_1, 'Количество': unit_2}
            self.my_unit.update(unique)
            self.my_warehouse.append(self.my_unit)
            print(f'Текущее наполнение -\n {self.my_warehouse}')
        except:
            return f'Не верные данные!'
        print(f'Для выхода - !, продолжение - Enter')
        q = input(f'---> ')
        if q == '!' or q == 'q':
            self.my_warehouse_full.append(self.my_warehouse)
            print(f'Весь склад -\n {self.my_warehouse_full}')
            return f'Выход'
        else:
            return Warehouse.receiving(self)


class Printer(Warehouse):
    def to_print(self):
        return f'to print smth {self.lists_num} times'


class Scanner(Warehouse):
    def to_scan(self):
        return f'to scan smth {self.lists_num} times'


class Copier(Warehouse):
    def to_copier(self):
        return f'to copier smth  {self.lists_num} times'


unit_1 = Printer('Canon', 3000, 7, 15)
unit_2 = Scanner('Canon', 1500, 2, 10)
unit_3 = Copier('Canon', 1000, 4, 15)
print(unit_1.receiving())
print(unit_2.receiving())
print(unit_3.receiving())
print(unit_1.to_print())
print(unit_3.to_copier())
