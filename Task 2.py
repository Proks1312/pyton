def personal_data(**kwargs):
    return ''.join(kwargs.values())


print(personal_data(name=input("Введите ваше имя"), surname=input("Введите вашу фамилию"),
                    phone=input("Введите ваш номер телефона"), town=input("Введите город где вы проживаете"),
                    email=input("Введите вашу почту"), birthday=input("Введите вашу дату рождения")))
