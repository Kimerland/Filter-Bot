from prisma.models import GroupSetting
from app.data.database import db

DEFAULT_SETTINGS = {
    "short_mute": {"limit": 2, "duration": 2},
    "long_mute": {"limit": 6, "duration": 24},
}

async def get_group_update(chat_id: int) -> dict:
    setting = await db.groupsetting.find_unique(where={"chat_id": str(chat_id)})
    if not setting:
        return DEFAULT_SETTINGS
    
    return {
     "short_mute": {"limit": setting.short_limit, "duration": setting.short_hours},
     "long_mute": { "limit": setting.long_limit, "duration": setting.long_hours}
    }

async def update_group_setting(chat_id: int, setting_type: str, new_limit: int, new_duration: int):
    chat_id_str = str(chat_id)
    setting = await db.groupsetting.find_unique(where={"chat_id": chat_id_str})

    if not setting:
        await db.groupsetting.create(
            data={
                "chat_id": chat_id_str,
                "short_limit": new_limit if setting_type == "short_mute" else DEFAULT_SETTINGS["short_mute"]["limit"],
                "short_hours": new_duration if setting_type == "short_mute" else DEFAULT_SETTINGS["short_mute"]["duration"],
                "long_limit": new_limit if setting_type == "long_mute" else DEFAULT_SETTINGS["long_mute"]["limit"],
                "long_hours": new_duration if setting_type == "long_mute" else DEFAULT_SETTINGS["long_mute"]["duration"],
            }
        )
    else:
        data={}
        if setting_type == "short_mute":
            data = {"short_limit": new_limit, "short_hours": new_duration}
        elif setting_type == "long_mute":
            data = {"long_limit": new_limit, "long_hours": new_duration}

        await db.groupsetting.update(where={"chat_id": chat_id_str}, data=data)