def my_func():
    a = 0
    while True:
        checklist = input("Введите номер и 'k' для завершения").split()
        for i in checklist:
            if i.lower() == "k":
                return a
            else:
                try:
                    a += int(i)
                except ValueError:
                    print("Для завершения работы введите - 'k'")
        print(f"Сумма значений = {a}")


print(my_func())
