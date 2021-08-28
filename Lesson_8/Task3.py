class ErrorNumber(ValueError):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список (для завершения работы введите "stop"):')
        if value == 'stop':
            break
        if not value.isdigit():
            raise ErrorNumber(value)
        my_list.append(int(value))
    except ErrorNumber as a:
        print('Это не число!', a)
print(my_list)
