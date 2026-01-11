import json

def get_next_id(users):
    if not users:
        return 1
    else:
        return max(user['id'] for user in users) + 1

class User():
    '''
    Класс для создания пользователя с ролью наставника 
    или стажера, заполнением чек-листа и расчетом среднего балла.
    '''

    def __init__(self, user_id):
        self.id = user_id
        self.role = self.choose_role()
        self.checklist = self.checklist_fill()
        self.avg = self.get_avg()
        
    def choose_role(self):
        choice_role = input('Выберите роль (mentor / trainee): ').strip().lower()

        while choice_role not in ('mentor', 'trainee'):
            choice_role = input('Ошибка. Выберите роль (mentor / trainee): ').strip().lower()
        
        return choice_role

    def checklist_fill(self):
        if self.role == 'mentor':
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
        
        return checklist
    
    def get_avg(self):
        return sum(self.checklist) / len(self.checklist)
    
    def get_user_data(self):
        self.user_data = {
            'id': self.id,
            'role': self.role,
            'avg': self.get_avg(),
            'checklists': {
                'mentor' if self.role == 'trainee' else 'trainee': self.checklist
            }
        }
        return self.user_data

    def user_output(self):
        print('Данные пользователя:')
        print(f'ID: {self.id}')
        print(f'Роль: {self.role}')
        print(f'Средний балл: {self.avg}')
        print(f'Чек-лист: {self.checklist}')

def load_data(filename='data/users.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []
    
def save_data(users, filename='data/users.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:    
        return []

users = load_data()
new_user = User(get_next_id(users))
users.append(new_user.get_user_data())
save_data(users)

new_user.user_output()
