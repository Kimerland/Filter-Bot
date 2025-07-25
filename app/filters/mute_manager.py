import json 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SETTINGS_PATH = BASE_DIR / "data" / "mute_settings.json"

def load_setting():
    if SETTINGS_PATH.exists():
        with open(SETTINGS_PATH, "r") as f:
            return json.load(f)
    return {}

def save_setting(data):
    print("Сохраняю настройки:", data)  
    with open(SETTINGS_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_group_update(chat_id):
    all_setting = load_setting()
    return all_setting.get(str(chat_id), {
     "short_mute": {"limit": 2, "duration": 2},
     "long_mute": { "limit": 6, "duration": 24}
    })

def update_group_setting(chat_id, setting_type, new_limit, new_duration):
    settings = load_setting()
    chat_settings = settings.get(str(chat_id), {})

    chat_settings[setting_type] = {
        "limit": new_limit,
        "duration": new_duration
    }
    
    settings[str(chat_id)] = chat_settings
    print(f"Сохраняю настройки для {chat_id}:", chat_settings)
    save_setting(settings)