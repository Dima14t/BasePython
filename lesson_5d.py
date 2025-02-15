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