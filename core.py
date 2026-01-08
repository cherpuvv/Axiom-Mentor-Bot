def create_user():
    
    id = 0

    choice_role = input('Выберите роль (mentor / trainee): ').strip().lower()

    while choice_role not in ('mentor', 'trainee'):
        choice_role = input('Ошибка. Выберите роль (mentor / trainee): ').strip().lower()
        id += 1

    if choice_role == 'mentor':
        checklist_key = 'trainee'
        print('Заполните чек-лист наставника (оцените стажера)')
    else:
        checklist_key = 'mentor'
        print('Заполните чек-лист стажера (оцените процесс)')

    checklist = []

    for i in range(5):
        rate = input(f'Введите оценку №{i + 1} от 1 до 5:')
        checklist.append(rate)
    
    user = {
        'id': id,
        'role': choice_role,
        'checklists': {
            checklist_key: checklist
        }
    }

    return user

users = []

new_user = create_user()
users.append(new_user)
print('\nСозданный пользователь:')
print(new_user)