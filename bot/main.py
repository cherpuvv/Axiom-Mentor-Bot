from bot.user import User
from bot.output import print_user, print_users, print_message
from storage.json_storage import load_users, save_users


def get_next_id(users: list) -> int:
    """
    Генерирует следующий id на основе сохранённых пользователей.
    """
    if not users:
        return 1
    return max(user["id"] for user in users) + 1


def main():
    # 1. Загружаем сохранённых пользователей
    users_data = load_users()

    print_message("Текущие пользователи в системе:")
    print_users(users_data)

    # 2. Создаём нового пользователя
    new_id = get_next_id(users_data)

    try:
        role = input("Введите роль пользователя (mentor / trainee): ").strip().lower()
        user = User(new_id, role)
    except ValueError as e:
        print_message(f"Ошибка создания пользователя: {e}")
        return

    # 3. Создаём чек-лист для пользователя
    checklist_name = "mentor" if user.role == "trainee" else "trainee"
    user.create_checklist(checklist_name)

    print_message(f"Заполнение чек-листа '{checklist_name}'")

    for i in range(5):
        while True:
            try:
                score = int(input(f"Введите оценку №{i + 1} (1–5): "))
                user.add_score_in_checklist(checklist_name, score)
                break
            except ValueError as e:
                print_message(f"Ошибка: {e}")

    # 4. Сохраняем пользователя
    users_data.append(user.get_user_data())
    save_users(users_data)

    # 5. Вывод результата
    print_message("\nПользователь успешно добавлен:")
    print_user(user.get_user_data())


if __name__ == "__main__":
    main()