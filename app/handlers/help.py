from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message 

router = Router()

@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "🛠 *Доступные команды:*\n"
        "/start — Приветствие и информация о боте\n"
        "/help — Показать это сообщение\n"
        "/status — Показать активные фильтры\n"
        "/settings — Групповые настройки\n\n"
        "_Для правильной работы бот должен быть администратором._",
        parse_mode="Markdown"
    )