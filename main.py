import asyncio
from chat import chat_with_ai
from os import getenv, system
from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from aiogram.types import Message

load_dotenv()
BOT_TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)
ai_status = True

@dp.message(Command("start"))
async def start_handler(message:Message) -> None:
    temp = await message.answer("The bot is starting ...")

    chat_id, message_id = temp.chat.id, temp.message_id
    await asyncio.sleep(2)
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text="Hello, how can i assist you today?"
        )
    
@dp.message(Command("suspend"))
async def shutdown_handler(message:Message) -> "It will shutdown pc":
    system("systemctl suspend")

@dp.message(Command("off_ai"))
async def ai_shutdown_handler(message:Message) -> "Shutdown ai -> ollama":
    system("systemctl stop ollama")
    global ai_status
    ai_status = False

@dp.message(Command("on_ai"))
async def ai_shutdown_handler(message:Message) -> "Shutdown ai -> ollama":
    system("systemctl start ollama")
    global ai_status
    ai_status = True

@dp.message()
async def response_from_chat(message:Message) -> "response":
    temp = await message.answer("Processing...")
    global ai_status
    if ai_status:
        chat_id, message_id = temp.chat.id, temp.message_id
        try:
            text = chat_with_ai(message.text, stream=0)
            print(message.text)
            print(text)
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=text
                )
        except Exception as e:print(e)
        return 0;
    else:
        await message.answer("Sorry, ai is down")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
