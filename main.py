import os
from modules.ideas import show_ideas, add_ideas

list_ideas = [
    {"name": "Трекер привычек", "topic": "Консольное приложение", "difficulty": "Легко"},
    {"name": "Клиент-серверное приложение", "topic": "UI приложение", "difficulty": "Средне"},
    {"name": "Обфускатор для питона", "topic": "Консольное приложение", "difficulty": "Сложно"},
]



def MaiN():
    while True:
        print("=== Каталог идей для Python-проектов ===")
        print('1. Вывести идеи\n2. Добавить идею\n3. Открыть проект на гитхабе\n4. Выйти')
        try:
            choice = int(input())
            if 0 < choice < 5:
                Logic(choice, list_ideas)
        except ValueError as v:
            print(f"{v}!")
            os.system("cls")
            MaiN()
def Logic(sa, ideas):
    if sa == 2:
        name = input("Введите имя новой идеи:   ")
        topic = input("Введите тему идеи:   ")
        difficulty = input("Введите сложность идеи: ")
        add_ideas(ideas, name, topic, difficulty)
    elif sa == 4:
        exit()
    elif sa == 3:
        print("")
    elif sa == 1:
        show_ideas(list_ideas)

MaiN()