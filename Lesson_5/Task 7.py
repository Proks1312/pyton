import json

with open("my_ex7.jons", "w", encoding="utf-8") as wr:
    with open("text_7.txt", encoding="utf-8") as obj:
        income = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in obj}
        res = [income, {"Средний доход": round(sum([int(a) for a in income.values() if int(a) > 0]) /
                                               len([int(a) for a in income.values() if int(a) > 0]))}]
    json.dump(res, wr, ensure_ascii=False, indent=4)
