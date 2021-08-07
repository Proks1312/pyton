chek_list = input("Введите числа списка с пробелом -").split()
for a in range(1, len(chek_list), 2):
    chek_list.insert(a - 1, chek_list.pop(a))

print("Обновленный список:", chek_list)
