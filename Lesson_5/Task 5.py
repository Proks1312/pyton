from random import randint

with open("Text_5.txt", "w", encoding="utf-8") as new_file:
    list = [randint(1, 1000) for _ in range(200)]
    new_file.write(" ".join(map(str, list)))
    print(f"Сумма всех чисел - {sum(list)}")
