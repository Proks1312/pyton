class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_str(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        date_a = cls(day, month, year)
        print(cls, date_str)
        return date_a

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3999:
            print(date_as_string)
            return day, month, year
        else:
            print('Ошибка ввода данных.Проверьте исходные данные ')


d = '28-12-2021'
date_b = Date.from_str(d)
is_date = Date.is_date_valid(d)

