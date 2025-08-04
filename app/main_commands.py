from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from app.filters.mute_manager import get_group_update
from app.filters.mute_manager import update_group_setting
from aiogram.types import CallbackQuery, Message

router = Router()
inputs = {}

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("👋 Приветствую!\n\n"
            "Добавьте этого бота в свою группу, в качестве админа чтобы фильтровать неправильное поведение.\n\n"
            "Если вы добавите этого бота в качестве администратора, он сможет удалять нежелательные сообщения, и ограничивать сообщения пользователя на определённое время.\n\n"
            "Вы можете установить индивидуальный лимит, а так же очищать лимиты для всех. По умолчанию:\n"
            "⚠️ 2-х и более удаления – мут 2 часа\n"
            "🚫 6-x и более удаления – мут 24 часа\n\n"
            "Создан @kimersed\n\n"
            "Хотите узнать больше /help?"
        )

@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "🛠 *Доступные команды:*\n\n"
        "/start — Перезапуск и нформация о боте\n"
        "/help — Показать сообщение с функционалом\n"
        "/settings — Групповые настройки\n\n"
        "_Помните, что для правильной работы бот должен быть администратором!_",
        parse_mode="Markdown"
    )

@router.message(Command("settings"))
async def cmd_settings(message: Message):
    chat_id = message.chat.id
    settings = await get_group_update(chat_id)

    inline_keyword = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Короткая фильтрация", callback_data="change_short")],
    [InlineKeyboardButton(text="Длинная фильтрация", callback_data="change_long")],
    [InlineKeyboardButton(text="Сбросить лимиты", callback_data="clear")],
    [InlineKeyboardButton(text="Отмена", callback_data="cancel")],
    ])

    text = (
         "⚙️ Текущие настройки фильтрации:\n\n"
        f"• Короткая фильрация: {settings['short_mute']['limit']} нарушений → {settings['short_mute']['duration']} ч.\n"
        f"• Длинная фильтрация: {settings['long_mute']['limit']} нарушений → {settings['long_mute']['duration']} ч.\n\n"
    )

    await message.answer(text, reply_markup=inline_keyword)

@router.callback_query(F.data.startswith("change_"))
async def change_setting(callback: CallbackQuery):
    raw_type = callback.data.replace("change_", "")
    setting_type = f"{raw_type}_mute"
    user_id = callback.from_user.id

    inputs[user_id] = {
        "setting_type": setting_type,
        "chat_id": callback.message.chat.id
    }

    await callback.message.answer(f"Введите новое значение для {setting_type} (формат: лимит, часы)")
    await callback.answer()


@router.message()
async def catch_setting_input(message: Message):
    user_id = message.from_user.id

    if user_id not in inputs:
        return
    
    try:
        data = inputs.pop(user_id)
        limit_str, hours_str = message.text.split(",")
        limit = int(limit_str.strip())
        hours = int(hours_str.strip())
    except Exception:
        await message.answer("❌ Неверный формат. Введите: 2, 4")
        return
    
    await update_group_setting(data["chat_id"], data["setting_type"], limit, hours)
    await message.answer(f"✅ Обновлено: {data['setting_type']} → {limit} нарушений за {hours} ч.")
