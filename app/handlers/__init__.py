from .mute_command import router as mute_router
from aiogram import Router

router = Router()
router.include_router(mute_router)