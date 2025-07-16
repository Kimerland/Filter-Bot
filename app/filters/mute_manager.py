import json 
from pathlib import Path

SETTINGS_PATH = Path("data/mute_settings.json")

def load_setting():
    if SETTINGS_PATH.exists():
        with open(SETTINGS_PATH, "r") as f:
            return json.load(f)
    return {}

def save_setting(data):
    with open(SETTINGS_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_group_update(chat_id):
    all_setting = load_setting()
    return all_setting.get(str(chat_id), {
     "short_mute": {"limit": 2, "duration": 2},
     "long_mute": { "limit": 6, "duration": 24}
    })

def update_group_setting(chat_id, limit, new_limit, new_duration):
    settings = load_setting()
    chat_settings = settings.get(str(chat_id), {})
    chat_settings[limit] = {
        "limit": new_limit,
        "duration": new_duration
    }
    settings[str(chat_id)] = chat_settings
    save_setting(settings)