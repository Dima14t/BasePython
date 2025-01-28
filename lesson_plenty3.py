# Множество - set() - {}

set_of_numbers = {1,2,2,2,3,4}
print(type(set_of_numbers))
print(set_of_numbers)

names = ['Ivan', 'Maria', 'Ivan']
print(set(names))


# создание множества при помощи функции set
set_of_names = set(['Ivan', 'Maria', 'Ivan'])
print(set_of_names)

print(len(set_of_names))

# добавление элемента во множество
set_of_names.add('Dima')
print(set_of_names)

# удаление элимента
# in - оператор, который проверяет вхождение элемента в коллекцию
if "Dima2" in set_of_names:
    set_of_names.remove('Dima2')
else:
    print("Такого элемента нет")

set_of_names.discard("Dima2")
print(set_of_names)

users_1 = {"Dima", "Vova", "Elena"}
users_2 = {"Dima", "Sasha", "Masha"}

# обЪединение множеств
# users_3 = users_1 | users_2
# print(users_3)

# перечисление множеств
# users_3 = users_1.intersection(users_2)
# & - операция логического умножения
# users_3 = users_1 & users_2
# print(users_3)

# intersection_update - сразу заменяет одно из множеств
# users_1.intersection_update(users_2)
# print(users_1)

# разность множеств
# users_3 = users_2.difference(users_1)
# users_3 = users_1 - users_2
# print(users_3)

# симметрическая разность множеств
# users_3 = users_1.symmetric_difference(users_2)
# print(users_3)
users_3 = users_1 ^ users_2
print(users_3)

users_4 = frozenset({"Masha", "Sasha"})
users_3 = frozenset(users_3)
users_3 = set(users_3)
print(type(users_3))
# print(type(users_3))
# int '5' -> 5 int('5') set()