# строки (string)
name = "Sasha"
lastname = 'Ivanov'
gender = 'm'

text = ("asfdsgfdfgfdgdfgdf"
        "dfgdfgdfgdfgdfgdfg"
        "dfgdfgdfgdfgdfgdfgdf"
        "dfgdfgdfgdfgdfgdfgd")

description = """
    dfdefdsgfds
    sgfdfgdfgdf
    dfgdfgdfg
    dfgdfgdf
"""
# print(type(text))
car = "bmw"
# print(id(car))
# print(car + ' 3')
# print(id(car))
# print(car)
# car += "x5"
# print(car)
# print(len(car))
# print(car[0])
# print(car[-1])
#
# print(car[:3])

# car += "x5"
# if car.find('3') != -1:
#         print('3')
# elif car.find('5') != -1:
#         print('5')
#
# print(car)

# print("aaaabbbb".count('aaaaaa'))
# print("bmwx5".index("x5xx"))
name = 'dima'
# print(name.title())
# print(name.upper())
# print("DIMA".lower())
#
# print("dima ivanov".title())
# print("Dima ivanov"[0].upper())
name_dima = "dima ivanov"

emails = [
        "user@mail.ru",
        "admin@gmail.com",
        "alex@yandex.ru"
]

# for email in emails:
#         if email.endswith("ru"):
#                 print(email)

# for email in emails:
#         if email.startswith("admin"):
#                 print(email)

a = "25"
b = "hello2"
print(a.isdigit())
print(b.isdigit())
print(b.isalpha())


age = "26a"
if age.isdigit():
        if int(age) < 30:
                print("ok")
else:
        print("Не является числом")


# my_text = "I Love love python"
# my_text_lower = my_text.lower()
# print(my_text.lower().count('l'))

my_string = "I,.love,   Python!"
print(my_string.split(","))

clean_list = []
for word in my_string.split(','):
    clean_list.append(word.strip('!.'))

print(clean_list)

my_list = ['mail', 'academy', 'ru']
site = ""
for word in my_list:
    site += word + '.'
site = site[:-1]
print(site)

site = ".".join(my_list)
print(site)

site = ".".join(my_list)
new_string = " - ".join(["bmw", "audi", "renavlt"])
print(new_string.split(" - "))
print(new_string)
stih = "sfdsfds\ndsdddsf\nddsssd\nrefef"
print(stih.splitlines)