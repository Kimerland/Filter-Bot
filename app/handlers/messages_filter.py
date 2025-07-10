from aiogram import Router, types, F
from aiogram.enums.chat_type import ChatType
from app.filters.ban_words import container_words

router = Router()

@router.message(F.chat.type.in_({ChatType.GROUP, ChatType.SUPERGROUP}))
async def handle_messages(message: types.Message):
    if not message.text:
        return

    if container_words(message.text):
        await message.delete()
        await message.chat.send_message(
            f"🚫 Сообщение от @{message.from_user.username or 'пользователя'} было удалено (запрещённые слова)"
        )
