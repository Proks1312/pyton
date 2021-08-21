from random import choice


class Car:
    movement = ["вперед", "назад", "влево", "вправо"]

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Автомобиль: {name}\n Цвет: {color}.\n Это полицейский автомобиль? {is_police}")

    def ride(self):
        print(f"{self.name}: погнал")

    def stop(self):
        print(f"{self.name}: остановилась")

    def direction(self):
        print(f"{self.name}:двигается {choice(self.movement)}.")

    def speed_reveal(self):
        print(f"{self.name}:двигается со скоростью {self.speed}.")


class TownCar(Car):
    """Легковой автомобиль"""

    def speed_reveal(self):
        return f'{self.name}:\n Скорость автомобиля {self.speed}.Превышение' if self.speed > 60 else \
            super().speed_reveal()


class WorkCar(Car):
    """Груовой автомобиль"""

    def speed_reveal(self):
        return f'{self.name}:\n Скорость автомобиля {self.speed}.Превышение' if self.speed > 40 else \
            super().speed_reveal()


class PoliceCar(Car):
    """Автомобиль ППС"""

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


class SportCar(Car):
    """Спортивый автомобиль"""


wor_car = WorkCar("Камаз", " желтый", 40)
pol_car = PoliceCar("UAZ Hunter", "бело-синий", 110)
t_car = TownCar("Mercedes с 200", "черный", 80)
s_car = SportCar("Ferrari f40", "черный", 365)

set_car = [wor_car, pol_car, t_car, s_car]
for k in set_car:
    k.ride()
    print(k.speed_reveal())
    k.direction()
    k.stop()
    print()
