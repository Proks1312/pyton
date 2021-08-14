from functools import reduce

print(reduce(lambda i, o: i * o, [n for n in range(100, 1001, 2)]))
