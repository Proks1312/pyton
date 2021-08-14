from itertools import count, cycle

count = count(3)
cycle = cycle("INO")
for _ in range(10):
    print("(сount,cycle)=({},{})".format(next(count), next(cycle)))
