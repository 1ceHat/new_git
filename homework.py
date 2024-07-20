from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

__API = open('secret.txt', 'r').read()
bot = Bot(token=__API)
dp = Dispatcher(bot, storage=MemoryStorage())

Help = '''
'''

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(messages):
    print('Введите команду /start, стобы начать.')


if __name__ == "__main__":
    executor.start_polling(dp)
