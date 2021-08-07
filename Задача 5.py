my_list = [9, 9, 8, 8, 7, 6, 5, 5, 4, 3, 3, 3, 2, 2, 1]
new_number = int(input("Введите новый номер в рейтинг (натуральное число) - "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
    else:
        break
my_list.insert(i, new_number)
print(my_list)
