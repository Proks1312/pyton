from random import randint

list = [randint(-10, 10) for _ in range(20)]
new_list = [num for num in list if list.count(num) == 1]
print(f"Исходный список\n{list}\nСписок без повторений\n{new_list}\n")
