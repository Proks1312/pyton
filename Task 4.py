def my_func(x, y):
    try:
        num = x ** y
    except TypeError:
        return "Введите действительное положительное (x) число и целое отрицательное число(y)"
    return num


print(my_func(5.2, -5))
