with open("Text_3.txt", "r", encoding="utf-8")as h:
    salary = {string.split()[0]: float(string.split()[1]) for string in h}
    print(
        f'f Средняя зарплата = {round(sum(salary.values())) / len(salary), 3}\n'
        f''f'Заработная плата меньше 20к {[a[0] for a in salary.items() if a[1] < 20000]}')
