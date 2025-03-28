# 1. создайте текстовый файл task_1.txt при помощи python.
# 2. запишите в него следующий текст: Пословицы – неотъемлемая часть
# повседневной речи каждого Русского человека.
# 3. считайте файл в программу
# 4. Выведите на экран следуюущую информацию с пояснениями:
# - первый символ текста
# - последний символ текста
# - первые три символа
# - последние три символа
# - первое слово
# - последнее слово
# - количество символов
# - количество слов
# - тест в верхнем регистре
# - текст в нижнем регистре

with open("task_1.txt", "r") as file:
    text = file.read()
print(text)  # - текст полностью
print(text[0],"- первый символ текста")

print(text[74],"- последний символ текста")

print(text[0:3],"- первые три символа")

print(text[-3:],"- последние три символа")

print(text[0:9],"- первое слово")

print(text[-9:-1],"- последнее слово")

text1 = len(text)
print("Количество символов - ",text1)

# Более точный подсчет слов смотрите в моем примере
# флаги:
# \b - граница слова
# \w+ - это класс символов
# findall - найти
# Модуль re в Python используется для работы с регулярными выражениями.
# Регулярные выражения (regex) — это последовательности символов,
# которые создают шаблоны для поиска и манипулирования текстом.
import re
text2 = text
words = re.findall(r'\b\w+\b', text2)

word_count = len(words)
print("Количество слов: ",word_count)

print("Текст в верхнем регистре = ",str.upper(text))

print("Текст в нижнем регистре = ",str.lower(text))
