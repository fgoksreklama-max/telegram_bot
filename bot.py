import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

TOKEN = os.environ.get("BOT_TOKEN", "8060643943:AAF36mzOKOYMWb6HTg1FnLt4usE9uvM-pWs")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Бот запущен!")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
