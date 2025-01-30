# Задания по работе с файлами в python:
#
# 1. Пользователь с клавиатуры вводит текст. Запишите этот текст в файл text1.txt.
# 2. Пользователь с клавиатуры вводит текст. Добавьте этот текст в конец файла text1.txt
# 3. Выведите на экран содержимое файла text1.txt

#  with - с
#  as - как
#  Задание 1: Запись текста в файл

text = input("Введите текст для записи в файл: ")
with open("text1.txt", "w") as file:  # w - режим записи (write)
    file.write(text)


# Задание 2: Добавление текста в конец файла

text = input("Введите текст для добавления в файл: ")
with open("text1.txt", "a") as file:  # a - режим добавления (append)
    file.write(text)


#  Задание 3: Вывод содержимого файла

with open("text1.txt", "r") as file: # r - режим чтения (read)
    content = file.read()
    print(content)