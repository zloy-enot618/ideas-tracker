def show_ideas(ideas):
    print("==== Список ваших идей =====")
    index = 0
    for index, idea in enumerate(ideas, start=1):
        print(f"{index}. Имя: {idea['name']} | Тип: {idea['topic']} | Сложность: {idea['difficulty']}")

def add_ideas(ideas, name, topic, difficulty):
    new_idea = {
        "name": name,
        "topic": topic,
        "difficulty": difficulty
    }
    ideas.append(new_idea)
    print(f"Успешно добавлена идея с именем: [{name}]!")