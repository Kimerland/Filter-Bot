from collections import defaultdict
from aiogram import Router, types
from aiogram.enums.chat_type import ChatType
from app.filters.ban_words import container_words
from app.filters.mute_manager import get_group_update
from app.services.gpt_filter import ask_gpt
from datetime import datetime, timedelta

messages_delete_counter = defaultdict(int)
router = Router()

@router.message()
async def filter_mute(message: types.Message):
    print("Фильтр сработал")

    if message.chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
        return
    
    if not message.text:
        return

    text = message.text.strip()
    
    if container_words(text):
        print("Найдено бан-слово")

        if await ask_gpt(text):
            print("GPT подтвердил — это пропаганда")
            try: 
                await message.chat.delete_message(message.message_id)
                print("Сообщение удалено")
            except Exception as e:
                print("Ошибка при удалении сообщения:", e)    
                

            chat_id = str(message.chat.id)
            user_id = message.from_user.id

            messages_delete_counter[(chat_id, user_id)] += 1
            count = messages_delete_counter[(chat_id, user_id)]
            settings = get_group_update(chat_id)

            if count >= settings["long_mute"]["limit"]:
                duration = settings["long_mute"]["duration"]
            elif count >= settings["short_mute"]["limit"]:
                duration = settings["short_mute"]["duration"]
            else:
                return 

            until_date = datetime.now() + timedelta(hours=duration)
            await message.bot.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user_id,
                permissions=types.ChatPermissions(can_send_messages=False),
                until_date=until_date
            )

            await message.answer(
                f"Пользователь @{message.from_user.username or 'без username'} замучен на {duration} ч. за {count} нарушений."
            )
        else:
            print("GPT is okay")

        
    print("container_words:", container_words(text))
