class Stationery:
    def __init__(self, title="определенным цветом"):
        self.title = title

    def draw(self):
        print(f'Начните рисовать {self.title} ')


class Pen(Stationery):
    def draw(self):
        print(f'Начните рисовать {self.title} ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f"Начните рисовать {self.title} карандашом")


class Handle(Stationery):
    def draw(self):
        print(f"Начните рисовать {self.title} маркером")


st = Stationery()
pen = Pen("синей")
pencil = Pencil("красным")
handle = Handle("черным")
office_supplies = [st, pen, pencil, handle]
for k in office_supplies:
    k.draw()
