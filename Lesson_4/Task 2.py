list = [25, 23, 5, 6, 7, 12, 10, 8, 11]
larger_num = [list[num] for num in range(1, len(list)) if list[num] > list[num - 1]]
print(larger_num)
