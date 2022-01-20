from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

bot = Bot(token=os.getenv('TOKEN'))
open_weather_token = os.getenv('OPW_TOKEN')
dp = Dispatcher(bot)