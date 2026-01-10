class User():
    '''
    Класс для создания пользователя с ролью наставника 
    или стажера, заполнением чек-листа и расчетом среднего балла.
    '''
    uid = 0

    def __init__(self):
        self.id = User.uid
        User.uid += 1
        self.role = self.choose_role()
        self.checklist = self.checklist_fill()
        self.avg = self.get_avg()
        self.user_data = {
            'id': self.id,
            'role': self.role,
            'avg': self.avg,
            'checklists': {
                'mentor' if self.role == 'trainee' else 'trainee': self.checklist
        }
    }
        
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
        return self.user_data

users = []
new_user = User()
users.append(new_user.get_user_data())
print('\nСозданный пользователь:')
print(new_user.get_user_data())