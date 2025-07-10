import asyncio
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from app.main_commands import router as commands_router 
from app.handlers import router as filter_router

dp = Dispatcher()
dp.include_router(commands_router)
dp.include_router(filter_router)
    

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())