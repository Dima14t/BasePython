print('Hello, World!')

b = 6
#a = 5s
name = 'Dima'
a = 24
print(a)
print(a - b)
print(a * b)
print(a / b)
print(a * b)
print(a % 2)

print('Hello')
print('Hi')
print(f"Hello. a = {a}")
print(f"Hello. a + b = {a + b}")

'''
fgfhfhfhf
'''

"""
Два раза на 2 ковыч получ 3
"""

c = 5.7
d = 7.0
print(type(a))
print(type(c))
print(type(c + a))

print(7 < 10)
print(7 > 10)
print(7 <= 10)
print(7 >= 10)
print(7 == 10)

# string
age = '24'
print(int(age) + 1)
last_name = "Ivanov sdfsdff dsfdsfdf"
text = "fdfdfdfff dkldkdd dsdddsd"

city = "Moscow\ncity"
print(city)

numbers = []
new_numbers = [1, 2, 3]
elements = [1, "2", 'name', True, [1, 2, 3]]
print(elements)

# КОРТЕЖ - не изменяемый список
colors = tuple()
new_colors = ("red", "blue", "green")

# словарь
car = {}
my_car = dict()
info = {"name": "Misha",
        "age": 26,
        "city": "Moscow",
        25: 46,
        ("1", 2, 3): 24,
        }

# в словаре не может быть двух одинаковых ключей
# ключом словаря может быть только неизменяемый тип данных

# set
set_of_names = {"Masha", "Sasha", "Dima", "Masha"}
print(type(set_of_names))
print(set_of_names)

cars = ['bmw', 'audi', 'bmw', 'bmw']
# list -> set
print(list(set(cars)))
txt = "Hello"
print(set(txt))

# if - elif - else
age = 16
if (age < 11 and age != 0):
    print("error")
elif age == 0:
    print("age == 0")
else:
    print("ok")

in_name = input("Введите ваше имя: ")
in_age = input("Введите ваш возраст: ")

print(f"Ваше имя - {in_name}")
print(f"Ваш возраст - {in_age}")
print(type(in_age))

print(12 == '12')