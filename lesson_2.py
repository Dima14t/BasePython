# словарь
person = {}
info = {"name": "Dima", "age": 26}

# получение элемента словаря
name = info["name"]
print(info["name"])

# добавленире элемента в словарь
info["phone"] = "8934949494"

# обновление значение элемента
info["name"] = "Sergey"

# размер словаря = кол-во элементов (пар, ключей)
print(len(info))
info["lang"] = ["russian", "english"]
print(info)
info["edu"] = {"hight": "MGU", "medium": "ITMO"}
print(info)

# ключом словаря может быть только неизменяймый тип данных (строка, число, кортеж)
cars = {("bmw", "audi"): "germany"}

age = info.pop("age")
print(age)
print(info)

#print(info["age"])
print(info.get("edu", "err").get("gjdkjj", {}))

print(info)

info_copy = info
print(info_copy)
print(id(info))
print(id(info_copy))
info["XXX"] = "YYY"
print(info_copy)

new_info = info.copy()
print(id(info))
print(id(new_info))

users = []
info_person = {}

for i in range(3):
  name = input("Введи имя: ")
  phone = input("Введи телефон: ")

info_person = {"name": name,"phone": phone}


users.append(info_person.copy())

print(users)

print(list(info.keys()))
print(list(info.values()))
print(list(info.items()))
info.update({"name": "sdsd", "age": 234})

for i in info:
    print(f"{i} - {info[i]}")

for key,value in info.items():
    print(f"{key} ---- {value}")

