def factorial(indicator):
    el = 1
    for a in range(indicator + 1):
        yield f'{a} = {el}'
        el *= a + 1


for index in factorial(int(input("Введите значение"))):
    print(index)
