def func():
    for a in input("Введите слова с пробелом (нижний регистр латиницы):\n").split():
        i = 0
        for i in a:
            if 95 <= ord(i) <= 120:
                i += 1
                print(a.title()) if i == len(a) else f"{a} - вводите только маленькие латинские буквы"


print(func())
