my_list = [(4 + 6j), 1, 1.2, True, None, "имя", frozenset(), range(10), (1, 2), ("возраст", "фамилия"),
           {"а", "б", "в", "г", "д"}, {"key_1": 500, 2: 400, "key_3": True, 4: None}
           ]
for a, chek in enumerate(my_list):
    print(f"{a}) {chek} - {type(chek)}")
