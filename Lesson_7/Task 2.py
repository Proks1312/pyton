from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, parameters):
        self.parameters = parameters

    @property
    @abstractmethod
    def cost(self):
        pass

    def __add__(self, other):
        Clothes.result += self.cost + other.cost
        return Suit(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"


class Coat(Clothes):
    @property
    def cost(self):
        return round((self.parameters / 6.5) + 0.5)


class Suit(Clothes):
    @property
    def cost(self):
        return round((2 * self.parameters + 0.3) / 100)


coat = Coat(55)
suit = Suit(190)
print(coat + suit + coat)
