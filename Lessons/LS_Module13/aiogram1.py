from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print('Urban сообщение')


@dp.message_handler(commands='allo')
async def start_messages(message):
    print('Стартовое сообщение')

@dp.message_handler()
async def all_messages(message):
    print('Мы получили сообщение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

