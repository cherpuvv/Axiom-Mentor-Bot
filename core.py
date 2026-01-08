def create_user():
    
    uid = 0

    choice_role = input('Выберите роль (mentor / trainee): ').strip().lower()

    while choice_role not in ('mentor', 'trainee'):
        choice_role = input('Ошибка. Выберите роль (mentor / trainee): ').strip().lower()

    uid += 1

    if choice_role == 'mentor':
        checklist_key = 'trainee'
        print('Заполните чек-лист наставника (оцените стажера)')
    else:
        checklist_key = 'mentor'
        print('Заполните чек-лист стажера (оцените процесс)')

    checklist = []
    checklist_size = 5

    for i in range(checklist_size):
        rate = int(input(f'Введите оценку №{i + 1} от 1 до 5:'))
        while rate not in (1, 2, 3, 4, 5):
            rate = int(input(f'Ошибка. Введите оценку №{i + 1} от 1 до 5:'))
        checklist.append(rate)
    
    user = {
        'id': uid,
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