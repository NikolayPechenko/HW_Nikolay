from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Информация')
button2 = KeyboardButton(text='Начало')
kb.add(button1)
kb.add(button2)
# kb.row, kb.insert() - чтобы выстраивать кнопки класиатуры в ряды, insert добавляет в конец ряда


@dp.message_handler()
async def start(message):
    await message.answer('Введите команду /start, чтобы начать общение')


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Информации пока нет')


@dp.message_handler(text='Начало')
async def start_message(message):
    await message.answer('Фильм хороший, посмотрите обязательно')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)