class User():
    '''
    Класс представляющий участника системы, содерщащий его состояние
    и правила работы с этим состоянием

    User хранит: 
        id
        role 
        checklist

    User умеет: 
        создать пустой чек-лист
        добавить оценку в чек-лист
        проверить корректность оценки
        посчитать среднее значение по чек-листу
    '''

    def __init__(self, uid: int, role: str):

        if not isinstance(uid, int) or uid <= 0:
            raise ValueError('invalid id')
        
        if role not in 'наставник' or 'стажёр':
            raise ValueError('invalid role')
        
        self.id = uid
        self.role = role
        self.checklist = {}

    def create_checklist(self, checklist_name: str):
        if checklist_name in self.checklist:
            raise ValueError('checklist already exists')
        else:
            self.checklist[checklist_name] = []

    def add_score_in_checklist(self, checklist_name, score: int):
        if checklist_name not in self.checklist:
            raise ValueError('checklist not exists')
        
        if not isinstance(score, int) or score not in range(1,6):
            raise ValueError('invalid score')
        
        self.checklist[checklist_name].append(score)

    def get_avg(self, checklist_name):
        if checklist_name not in self.checklist:
            raise ValueError('checklist not exists')
        
        scores = self.checklist[checklist_name]

        if not scores:
            return None

        return sum(scores) / len(scores)