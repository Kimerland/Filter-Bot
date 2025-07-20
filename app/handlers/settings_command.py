from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from app.filters.mute_manager import update_group_setting
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

router = Router()

class SettingState(StatesGroup):
    value = State()

@router.callback_query(F.data.startswith("change_"))
async def edit_setting_callback(callback: CallbackQuery, state: FSMContext):
    setting_type = callback.data.replace("change_", "").lower()

    await state.set_state(SettingState.value)
    await state.update_data(setting_type=setting_type, chat_id=callback.message.chat.id)

    await callback.message.answer(f"Введите новое значени для {setting_type} (формат: лимит, часы)\n\nПример: 2, 4")
    await callback.answer()

# add logic for update MemoryStorage