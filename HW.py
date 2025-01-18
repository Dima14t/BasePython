# Задание 1
# написать программу, которая запрашивает у пользователя номер месяца и выводит название
# этого месяца Если введено число 0 или число больше 12, то написать, что номер месяца
# должен быть от 1 до 12

# Запрашиваем у пользователя номер месяца
month_number = int(input("Введите номер месяца (от 1 до 12): "))

# Проверяем номер месяца и выводим название месяца
if month_number == 1:
    print("Январь")
elif month_number == 2:
    print("Февраль")
elif month_number == 3:
    print("Март")
elif month_number == 4:
    print("Апрель")
elif month_number == 5:
    print("Май")
elif month_number == 6:
    print("Июнь")
elif month_number == 7:
    print("Июль")
elif month_number == 8:
    print("Август")
elif month_number == 9:
    print("Сентябрь")
elif month_number == 10:
    print("Октябрь")
elif month_number == 11:
    print("Ноябрь")
elif month_number == 12:
    print("Декабрь")
else:
    print("Номер месяца должен быть от 1 до 12.")

# Задание 2
# написать программу, которая запрашивает у пользователя его имя, фамилию, возраст Вывести
# полученные данные на экран Если возраст, меньше 18, дополнительно вывести сообщение об этом

in_name = input("Имя - ")
in_nameF = input("Фамилия - ")
in_age = int(input("Возраст - "))
if in_age < 18:
    print(" Вам меньше 18 ! Ата та ! ")
else:
    print(" Вам есть 18 ")