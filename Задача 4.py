point = input("введите слова с пробелом").split()
for a, y in enumerate(point, 1):
    print(a, y) if len(y) <= 10 else print(a, y[:10])
