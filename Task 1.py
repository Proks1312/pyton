def splitting(parameter1, parameter2):
    try:
        parameter1, parameter2 = int(parameter1), int(parameter2)
        splitting_num = parameter1 / parameter2
    except ValueError:
        return "Ошибка в значении"
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    return round(splitting_num, 4)


print(splitting(input("введите число"), input("Введите число на которое хотите поделить")))
