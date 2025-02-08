# 1. Написать функцию, которая возвращает факториал числа
# 2. Написать функцию, которая принимает строку и возвращает количество символов в ней
# 3. Написать функцию, которая принимает имя, фамилию, возраст
#    и возвращает словарь с этими данными
# 4. Написать функцию, которая принимает 3 числа и возвращает словарь,
#    в котором содержится информация о сумме этих чисел, максимальном числе, минимальном числе

# def - функция

# Пример (1.0)
# def f():
#     a=9
#     b=1
#     print(a+b)
# f()

# 1
def factorial():
    n = int(input("Введите число для вычисления факториала: "))
    num = 1
    for i in range(1, n + 1):
        num *= i
    print(f"Факториал {n} равен {num}")

factorial()

# 2
def function():
    n = input("Напишите сюда строку: ")
    print(f"Количество символов в ней: {len(str(n))}")
function()

# 3
def function():
    name = input("Введите имя: ")
    family = input("Введите фамилию: ")
    age = int(input("Введите возраст: "))
    dictionary = {"name": name,"family": family, "age": age}
    print(dictionary)
function()

# 4
def function():
    one_1 = float(input("Введите первое число - "))
    two_2 = float(input("Введите второе число - "))
    three_3 = float(input("Введите третье число - "))

    numbers = [one_1, two_2, three_3]

    n = sum(numbers)
    max_num = max(numbers)
    min_num = min(numbers)

    dictionary = {
        "Первое_ч": one_1,
        "Второе_ч": two_2,
        "Третье_ч": three_3,
        "Cумма": n,
        "Максимальное_ч": max_num,
        "Минимальное_ч": min_num
    }

    print(dictionary)

function()
