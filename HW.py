# Дописать программу таким образом, чтобы в случае корректного имени выводилось сообщение
# в формате: Имя Elena относится к женскому полу с вероятностью 99%
# В случае некорректного имени выводилось сообщение Имя введено не корректно.

import requests


def get_data(name: str):
    url = f"https://api.genderize.io?name={name}"
    response = requests.get(url)
    data = response.json()
    return data

def parse_data(data: dict):
    name = data.get('name')
    gender = data.get('gender')
    probability = data.get('probability')
    probability_number = int(probability * 100)

    if gender:
        gender_rus = "мужскому" if gender == "male" else "женскому"
        print(f" Имя {name} относится к {gender_rus} полу. С вероятностью {probability_number}% . ")
    else:
        print("Имя введено не корректно.")


name = input("Введите имя: ")
data = get_data(name)
parse_data(data)
