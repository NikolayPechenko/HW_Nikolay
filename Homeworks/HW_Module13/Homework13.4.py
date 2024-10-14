from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1)
kb.insert(button2)


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands='start')
async def set_sex(message):
    await message.answer('Привет, я бот, помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler(text='Информация')
async def set_sex(message):
    await message.answer('Информации нет, но вы держитесь')


@dp.message_handler(text='Рассчитать')
async def set_sex(message):
    await message.answer('Введите свой пол (м/ж)')
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    await state.update_data(sex=message.text)
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=float(message.text))
    await message.answer("Введите свой рост (в см)")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=float(message.text))
    await message.answer("Введите свой вес (в кг)")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    if data['sex'] in ('М', 'м'):
        clr = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    else:
        clr = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161
    await message.answer(f"Ваша норма калорий - {clr}")
    await state.finish()

@dp.message_handler()
async def set_sex(message):
    await message.answer('Привет, я бот, помогающий твоему здоровью', reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
