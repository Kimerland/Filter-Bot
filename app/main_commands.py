from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("👋 Приветствую!\n\n"
            "Добавьте этого бота в свою группу, в качестве админа чтобы фильтровать неправильное поведение.\n\n"
            "Если вы добавите этого бота в качестве администратора, он сможет удалять нежелательные сообщения, и мутить пользователя на определённое время.\n\n"
            "Вы можете установить индивидуальный лимит, а так же обновлять для всех. По умолчанию:\n"
            "⚠️ 2-х и более удаления – мут 2 часа\n"
            "🚫 6-x и более удаления – мут 24 часа\n\n"
            "Создан @kimersed\n\n"
            "Хотите узнать больше /help?"
        )

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

# change on custom
@router.message(Command("status"))
async def cmd_status(message: Message):
    await message.answer(
        "⚙️ Настройки фильтрации:\n"
        "— Мут за 2 нарушения: 2 часа\n"
        "— Мут за 6 нарушений: 24 часа"
    )

@router.message(Command("settings"))
async def cmd_settings(message: Message):
    await message.answer("⚙️ В будущем здесь можно будет настраивать лимиты нарушений и мутов.")
