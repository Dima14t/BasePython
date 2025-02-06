# Дан файл со стихотворением poem.txt.
# Необходимо провести анализ текста и результат вывести на экран с пояснениями.
#
# 1. Сколько всего символов в тексте
# 2. Сколько букв в тексте (без пробелов и знаков препинания (,.!?))
# 3. Сколько всего строк в тексте
# 4. Сколько непустых строк в тексте
# 5. Сколько всего слов в тексте
# 6*. Сколько слов в каждой строке
# 7*. Сколько символов в каждой строке
# 8. Найти повторяющиеся слова в тексте с указанием количества
# 9*. Провести частотный анализ букв (частота появления какждой буквы в тексте)
# 10. Найти все посторонние символы (пробелы и знаки препинания) - какие и сколько

with open("poem.txt","r") as file:
    text = file.read()
    print(text) # текст в виде примера
# 1
text1 = len(text) # len - считает сколько всего символов(в том числе и пробелы, запят)
print("Всего символов в тексте:",text1)
# 2
import re # findall - найтивсе
text2 = text
words1 = re.findall(r"[а-яА-ЯёЁ]",text2)
print("букв в тексте (без пробелов и знаков препинания (,.!?)) - ",len(words1))
# 3
import re
text3 = text
words2 = len(re.findall(r"\n",text3))+1
print("Всего строк в тексте (с пробелами) - ",words2)
# 4
import re # findall - найтивсе
text4 = text
words3 = re.findall(r".+" ,text4)
print("Всего строк в тексте (без пробелов)- ",len(words3))
# 5
import re
text5 = text
words4 = re.findall(r"\b\w+\b",text5)
print("Всего слов в тексте:",len(words4))
# 6
# enumerate - Перечисление
# split - разделит строку на части: "Привет мир" -> ["Привет", "мир"]
import re
text6 = text
for i, line in enumerate(text6.split("\n"),+1):
    print(f"Строке слов - {i}: {len(re.findall(r"\S+",line))}")
# 7

text7 = text
for i, line in enumerate(text7.split("\n"),+1):
    print(f"Строке символов - {i}: {len(line)}")
# 8
# count - рассчитывать
import re
from collections import Counter
# из коллекции import счетчик - from collections import Counter
# lower - считывает слова "Как" и "как" (как одно единое целое слово)
word_counts = Counter(re.findall(r'\b\w+\b', text.lower()))

for word, count in word_counts.items():
    if count > 1:
        print(f"Слово: {word} и количество: {count}")
# 9
import re
from collections import Counter

     # Приводим текст к нижнему регистру и выбираем только буквы
filtered_text =''.join(filter(str, text.lower()))
     # filter - True или False (смотря что фильтровать должно быть условие)
     # "join" - words = ['Привет', 'мир'] => Вывод: 'Привет мир'
     # lower - считывает слова "Как" и "как" (как одно единое целое слово)
letter_counts = Counter(filtered_text)

for letter, count in letter_counts.items():
    print(f"Буква '{letter}': {count} раз(а)")
# 10

import re # findall - найтивсе
text8 = text
words5_1 = re.findall(r"\ ",text8)
words5_2 = re.findall(r"\,",text8)
words5_3 = re.findall(r"\.",text8)
words5_4 = re.findall(r"\-",text8)
words5_5 = re.findall(r"\:",text8)
print("Пробелы - ",len(words5_1))
print("Запятые - ",len(words5_2))
print("Точка - ",len(words5_3))
print("Тире - ",len(words5_4))
print("Двоеточие - ",len(words5_5))

# Пример вывода:
# 1. Всего символов в тексте - 670
# 2. Букв в тексте - 500
# 3. Всего строк в тексте - 40
# 4. Непустых строк в тексте - 30
# 5. Всего слов в тексте - 100
# 6. Анализ слов по строкам:
# 1 строка - 5 слов
# 2 строка - 4 слова
# 3 строка - 6 слов
# ....
# 7. Анализ символов по строкам:
# 1 строка - 25 символов
# 2 строка - 16 символов
# ....
# 8. Повторяющиеся слова:
# как - 2
# и - 8
# а - 6
# или - 3
# 9. Частотный анализ текста:
# а - 34
# б - 27
# в - 15
# г - 13
# ...
# 10. Прочие символы:
# пробелов - 56
# . - 16
# , - 34
# - - 25
# : - 4