class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            raise Error("Делить на ноль нельзя!")
        else:
            res = num_1 / num_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except Error as err:
        return err


print(division()) 
