import asyncio
from os import getenv, system

from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message:Message) -> None:
    await message.answer("The bot is starting ...")
    try:await system("ollama serve")
    except Exception as e:print(e)

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())