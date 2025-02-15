# 1. Написать функцию, которая возвращает, сколько дней осталось до нового года
# 2. Написать функцию, которая принимает дату рождения и возвращает количество полных лет
# 3. Написать функцию check_date(), которая принимает дату в формате строки "дд.мм.гггг"
# и возвращает количество дней, которые прошли с этой даты или сколько дней осталось)
#
# 4.
# 4.1 Написать функцию, которая принимает информацию о книге из консоли
# (автор, название, год, жанр)
# 4.2 Написать функцию, которая сохраняет в словарь информацию о книге с валидацией года
#     (1500 < год < текущий)
# 4.3 Сохранить в новый словарь информацию о 5 книгах
#     {
# 	"1": {
# 		"author": "Pushkin",
# 		"title": "Ruslan & Ludmila",
# 		....
# 	},
# 	"2": ...
#
#     }
# 4.5 Записать информацию о 5 книгах в books.json
# 4.6 Считать инф-ю из books.json в консоли

# 1

from datetime import datetime

def datetime_new():
    today = datetime.today()
    print(today)

    year = today.year - today.year
    month = 12 - today.month
    day = 31 - today.day
    hour = 23 - today.hour
    minute = 59 - today.minute
    second = 59 - today.second

    print(f"Осталось до Нового года: {year} Год, {month} Месяц, {day} День, "
          f"{hour} Час, {minute} Минуты, {second} Секунды")

datetime_new()

# 2
from datetime import datetime

def datetime_new():
    today = datetime.today()
    print(today)

    age_d  = int(input("Введите свой возраст(День)"))
    age_m = int(input("Введите свой возраст(Месяц)"))
    age_y = int(input("Введите свой возраст(Год)"))

    y = today.year - age_y

    print(f"День {age_d}, Месяц {age_m},  Лет {y}")

datetime_new()

# 3
from datetime import datetime

def check_date():
    date_str = input("дд.мм.гггг >>> ")
    date_obj = datetime.strptime(date_str, "%d.%m.%Y")

    delta = (datetime.today() - date_obj).days
    return delta

print(check_date())
#4 - текущ
# 4.1

from datetime import datetime

def dictionary():
    # Получаем информацию о книге от пользователя
    author, title, year, genre = input("Введите информацию о книге (автор, название, год, жанр): ").split(", ")
    print(f"Автор: {author}, Название: {title}, Год: {year}, Жанр: {genre}")

# текущая дата
today = datetime.today()

OT = int(input("Введите год: "))

if OT < 1500:
    print(f"Этот год меньше 1500 - {OT}")

#  словарь
dictionary = {
    "1500 > ": OT,
    "Текущий год": today.year
}

print(dictionary)

dictionary()

# 4.3

def book_dictionary():
    books = []
    for i in range(5):
        author = input(f"Книга({i+1}) Введите автора: ")
        title = input(f"Книга({i+1}) Введите заголовок: ")
        book = { "Автор": author, "Заголовок": title }
        books.append(book)
    print(books)

book_dictionary()

# 4.5

# Вот пример того, как можно записать информацию о 5 книгах
# в файл books.json на языке Python:

import json

# Данные о книгах
books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genre": "Fiction"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Fiction"
    },
    {
        "title": "Moby Dick",
        "author": "Herman Melville",
        "year": 1851,
        "genre": "Adventure"
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "year": 1869,
        "genre": "Historical Fiction"
    }
]

# Запись данных в файл books.json
with open('books.json', 'w') as json_file:
    json.dump(books, json_file, indent=4)

print("Данные о книгах успешно записаны в books.json.")

# Этот код создает список из 5 книг с их заголовками, авторами,
# годами публикации и жанрами, а затем записывает эти данные в
# файл books.json в формате JSON.

# 4.6

# Для выполнения этих задач, Вам нужно создать файл books.json и записать в
# него информацию о 5 книгах, а затем написать код для чтения этой информации и вывода в консоль.
# Вот пример, как это можно сделать на языке Python.
# 1. Запись информации о 5 книгах в books.json


import json

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "Moby Dick", "author": "Herman Melville", "year": 1851},
    {"title": "War and Peace", "author": "Leo Tolstoy", "year": 1869}
]

with open('books.json', 'w') as f:
    json.dump(books, f, indent=4)

# 2. Чтение информации из books.json и вывод в консоль

Python

import json

with open('books.json', 'r') as f:
    books = json.load(f)
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

# Объяснение:
#
#     В первом блоке кода мы создаем список словарей, где каждый словарь представляет книгу
#     с её заголовком, автором и годом издания. Затем мы записываем этот список в файл books.json.
#     Во втором блоке кода мы открываем файл books.json,
#     загружаем данные и выводим информацию о каждой книге в консоль.

