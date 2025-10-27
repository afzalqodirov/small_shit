import asyncio
from chat import chat_with_ai
from os import getenv
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from aiogram.types import Message


BOT_TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)
chat_id = 0
message_id = 0

@dp.message(Command("start"))
async def start_handler(message:Message) -> None:
    temp = await message.answer("The bot is starting ...")

    global chat_id, message_id
    chat_id, message_id = temp.chat.id, temp.message_id
    
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text="Hello, how can i assist you today?"
        )
    
@dp.message()
async def response_from_chat(message:Message) -> "response":
    for stream in chat_with_ai(message.text):
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=stream
        )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
