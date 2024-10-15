from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button1)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='info')],
        [
            KeyboardButton(text='shop'),
            KeyboardButton(text='donate')
        ]
    ], resize_keyboard=True
)


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Рады вас видеть', reply_markup=start_menu)


# @dp.callback_query_handler(text='info')  # тот текст, который указаан в callback_data
# async def info(call):  # это не сообщения, а вызов
#     await call.message.answer('Информация о боте')  # то, что будет в ответе на клик кнопки
#     await call.answer()









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)