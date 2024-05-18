import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_TOKEN = "6254948307:AAER6I_9bMTJTNAk3uWhSvT2VYJX_-JgeW4"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
