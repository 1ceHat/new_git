from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

__API = open('secret.txt', 'r').read()
bot = Bot(token=__API)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)

kb.add(KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация'))

Help = '''
'''


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.reply('Введите свой возраст (полные года)')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост в сантиметрах')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=float(message.text))
    await message.answer('Введите свой вес в килограммах')
    await UserState.weight.set()



@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=float(message.text))
    data = await state.get_data()
    male_calories = 10*data['weight'] + 6.25*data['growth'] - 5*data['age'] + 5
    female_calories = 0*data['weight'] + 6.25*data['growth'] - 5*data['age'] + 161
    await message.answer(f'Ваша ежедневная норма калорий:\n🔵{male_calories} - если Вы мужчина'
                         f'\n🟣{female_calories} - если Вы женщина')
    await state.finish()



@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, стобы начать.')


if __name__ == "__main__":
    executor.start_polling(dp)
