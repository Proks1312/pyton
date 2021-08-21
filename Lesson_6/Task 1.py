import time
import itertools


class TrafficLight:
    __color = [["Красный", [7, 31]], ["Желтый", [2, 33]], ["Зеленый", [5, 32]]]

    def go(self):
        for k in itertools.cycle(self.__color):
            print(f"\r\033[{k[1][1]}m\033[1m{k[0]}\033[0m", end="")
            time.sleep(k[1][0])


tr = TrafficLight()
tr.go()
