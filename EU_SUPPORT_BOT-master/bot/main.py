import aiogram
import requests
from aiogram import Dispatcher, Bot
from aiogram import types
from aiogram.utils import executor

TOKEN = '5684707655:AAFhnk87us1WhWiLYqASCw1OL_8MWb5Ps-A'

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привіт!\nТебе вітає підтримка Європейського Університету!\nРозкажи, що сталося?")



@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("Пошук вiльних операторiв")


if __name__ == '__main__':
    executor.start_polling(dp)