from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.add(button1)
kb.insert(button2)
kb.add(button3)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton(text='Рассчитать номру калорий', callback_data='calories')
button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb2.add(button1)
kb2.insert(button2)

kb3 = InlineKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button2 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button3 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button4 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
kb3.row(button1, button2, button3, button4)


class UserState(StatesGroup):
    sex = State()

    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=kb2)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5\n '
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161 '
                              )
    await call.answer()


@dp.message_handler(commands='start')
async def set_sex(message):
    await message.answer('Привет, я бот, помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler(text='Информация')
async def set_sex(message):
    await message.answer('Информации нет, но вы держитесь')


@dp.callback_query_handler(text='calories')
async def set_sex(call):
    await call.message.answer('Введите свой пол (м/ж)')
    await call.answer()
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


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    list1 = ['beauty', 'Collagen', 'D3', 'Omega']
    for i in range(1, 5):
        with open(f'photos/{list1[i-1]}.jpeg', 'rb') as img:
            await message.answer(f'Название: {all[i-1][1]} | Описание: {all[i-1][2]} | Цена: {all[i-1][3]}')
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки: ', reply_markup=kb3)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def set_sex(message):
    await message.answer('Привет, я бот, помогающий твоему здоровью', reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
