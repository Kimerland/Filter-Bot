import asyncio
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from app.handlers import start, help
import logging

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(help.router)
    

async def main() -> None:
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())