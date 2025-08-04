import asyncio
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from app.main_commands import router as commands_router 
from app.handlers import router as handlers_router
from app.data.database import db

dp = Dispatcher()
dp.include_router(commands_router)
dp.include_router(handlers_router)  

async def main() -> None:
    await db.connect()
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())