def print_user(user_data: dict):
    """
    Выводит информацию об одном пользователе.
    Принимает данные пользователя в виде dict.
    """

    print("------ Пользователь ------")
    print(f"ID: {user_data.get('id')}")
    print(f"Роль: {user_data.get('role')}")

    checklists = user_data.get("checklists", {})

    if not checklists:
        print("Чек-листы отсутствуют")
        return

    for checklist_name, scores in checklists.items():
        print(f"\nЧек-лист: {checklist_name}")

        if not scores:
            print("  Оценок нет")
            continue

        print(f"  Оценки: {scores}")
        avg = sum(scores) / len(scores)
        print(f"  Средний балл: {avg:.2f}")


def print_users(users: list):
    """
    Выводит список пользователей.
    Принимает список словарей пользователей.
    """

    if not users:
        print("Пользователей нет")
        return

    for user in users:
        print_user(user)
        print("--------------------------")


def print_message(message: str):
    """
    Универсальный вывод сообщений.
    """
    print(message)