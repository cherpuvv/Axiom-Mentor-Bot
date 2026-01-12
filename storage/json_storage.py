import json

def load_users(filename = 'data/users.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []
    
def save_users(users, filename = 'data/users.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=4)

    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        return []