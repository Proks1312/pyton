tran_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("Text_343.txt", "w", encoding="utf-8") as j:
    with open("Text_4.txt", encoding="utf-8") as k:
        k.writelines([string.replace(string.split()[0], tran_rus.get(string.split()[0])) for string in k])
