from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

# ----- Settings ------
__API = open('secret.txt', 'r').read()
bot = Bot(token=__API)
dp = Dispatcher(bot, storage=MemoryStorage())
Help = '''
/start = запуск бота
'''


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
# --------------------

# ------ Keyboards ------


reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
inline_keyboard = InlineKeyboardMarkup(row_width=4)

reply_keyboard.add(KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация'))
inline_keyboard.add(InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
                    InlineKeyboardButton(text='Формулы', callback_data='formulas'))

# -------------------------


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=reply_keyboard)


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (полные года)')
    await UserState.age.set()
    await call.answer()


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
    male_calories = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
    female_calories = 0 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161
    await message.answer(f'Ваша ежедневная норма калорий:\n🔵{male_calories} - если Вы мужчина'
                         f'\n🟣{female_calories} - если Вы женщина')
    await state.finish()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10*вес (кг) + 6.25*рост (см) - 5*возраст (г) [+5, если мужчина / -161, если женщина]')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать.')


if __name__ == "__main__":
    executor.start_polling(dp)
