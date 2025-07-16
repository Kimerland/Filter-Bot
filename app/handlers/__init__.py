from .messages_filter import router as messages_router
from .mute_command import router as mute_router

from aiogram import Router

router = Router()
router.include_router(mute_router)
router.include_router(messages_router)