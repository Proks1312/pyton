dict = {}
with open("text_6.txt", encoding="utf-8") as k:
    for string in k:
        title, score = string.split(":")
        title_sum = sum(map(int, ''.join([a for a in score if a == "" or "9" >= a >= "0"]).split()))
        dict[title] = title_sum
        print(f'{dict}')
