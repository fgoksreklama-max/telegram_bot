import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8060643943:AAF36mzOKOYMWb6HTg1FnLt4usE9uvM-pWs"
bot = Bot(token=TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню"), KeyboardButton(text="Помощь")],
        [KeyboardButton(text="Время"), KeyboardButton(text="Курс")],
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я бот с клавиатурой.", reply_markup=keyboard)

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Команды: /start, /help, /info")

@dp.message(lambda msg: msg.text == "Меню")
async def menu_btn(message: types.Message):
    await message.answer("Выбери команду: /start, /help, /info")

@dp.message(lambda msg: msg.text == "Время")
async def time_btn(message: types.Message):
    from datetime import datetime
    await message.answer(f"Сейчас {datetime.now().strftime('%H:%M:%S')}")

@dp.message(lambda msg: msg.text == "Курс")
async def course_btn(message: types.Message):
    await message.answer("Курс доллара ≈ 80₽")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
