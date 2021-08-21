class Driveway:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def covering_entire_roadway(self, thickness=30, heft=10):
        return f"{self._length} метров * {self._width} метров * {heft} килограмм * {thickness} сантиметров = " \
               f"{(self._length * self._width * heft * thickness) / 1000} тонн"


drv = Driveway(7000, 25)
print(drv.covering_entire_roadway())
