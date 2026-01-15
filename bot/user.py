class User:
    """
    Модель пользователя системы.
    """

    def __init__(self, uid, role):
        # --- Валидация идентификатора ---
        if not isinstance(uid, int) or uid <= 0:
            raise ValueError('invalid id')

        # --- Канонические роли внутри системы ---
        if role not in ('mentor', 'trainee'):
            raise ValueError('invalid role')

        self.id = uid
        self.role = role

        # Хранилище чек-листов пользователя
        self.checklist = {}

    # ------------ Работа с чек-листами ------------

    def create_checklist(self, checklist_name: str):
        """
        Создаёт новый чек-лист для пользователя.
        """
        if checklist_name in self.checklist:
            raise ValueError('checklist already exists')

        self.checklist[checklist_name] = []

    def add_score_in_checklist(self, checklist_name, score: int):
        """
        Добавляет оценку в существующий чек-лист.
        """
        if checklist_name not in self.checklist:
            raise ValueError('checklist not exists')

        if not isinstance(score, int) or score not in range(1, 6):
            raise ValueError('invalid score')

        self.checklist[checklist_name].append(score)

    def get_avg(self, checklist_name):
        """
        Возвращает средний балл по чек-листу.
        """
        scores = self.checklist.get(checklist_name, [])

        if not scores:
            return 0.0

        return sum(scores) / len(scores)

    # ------------ Сериализация данных ------------

    def get_user_data(self):
        """
        Возвращает данные пользователя в виде dict.
        Используется для сохранения в JSON или передачи наружу.
        """
        return {
            "id": self.id,
            "role": self.role,
            "checklists": self.checklist
        }
