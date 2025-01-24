# 1 Напишите программу, которая принимает от пользователя его имя,
# фамилию, отчество, дату рождения и город. Запишите эти данные
# в словарь. В цикле выведите их со словаря на экран.
# Отдельно выведите фамилию и имя



name = input("Введите имя: ")
family = input("Введите фамилию: ")
patronymic = input("Введите отчество: ")
dateOfBirth = input("Введите дату рождения: ")
city = input("Введите город: ")

user = []  # - массив
info_person = {"Введите имя": name, "Введите фамилию": family, "Введите отчество": patronymic,
        "Введите дату рождения": dateOfBirth, "Введите город": city} #  - Словарик

print("Данные пользователя:")
for key, value in info_person.items():
    print(f"{key}: {value}")


user.append(info_person.copy())
print("Словарь ", user)
print("Фамилия и имя - ",family, name)

