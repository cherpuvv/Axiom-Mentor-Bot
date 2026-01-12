'''
    1. загрузить пользователей
    2. определить следующий id
    3. спросить роль
    4. создать пользователя
    5. создать нужный чек-лист
    6. собрать оценки
    7. сохранить пользователя
'''

from bot.user import User
from bot.output import print_user
from storage.json_storage import load_users, save_users

users = load_users()

def get_id(users):
    if not users:
        return 1
    else:
        return int(max(user['id'] for user in users)) + 1
    
def get_role():
    role = input('Выберите вашу роль "Наставник" или "Стажёр": ').strip().lower()

    if role not in ('наставник' or 'стажёр' or 'стажер'):
        raise ValueError('Роль введена неверно')
    
    return role

uid = get_id(users)
role = get_role()

user = User(uid, role)