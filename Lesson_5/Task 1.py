with open("text_1.txt", "w", encoding='utf-8') as k:
    while True:
        string = input("Введите строку или введите пустую строку для завершения работы: ")
        if not string:
            break
            print(string, file=k)
