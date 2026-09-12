def show_ideas(ideas):
    None

def add_ideas(ideas, name, topic, difficulty):
    new_idea = {
        "name": name,
        "topic": topic,
        "difficulty": difficulty
    }
    ideas.append(new_idea)
    print(f"Успешно добавлена идея с именем: [{name}]!")