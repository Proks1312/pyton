with open("Text_2.txt", "r", encoding="utf-8") as k:
    inf = [f"{string}. {number.strip()} - {len(number.split())} слов" for string, number in enumerate(k, 1)]
    print(*inf, f"Всего строк - {len(inf)}.", sep="\n")
