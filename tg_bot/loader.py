from aiogram import Bot, Dispatcher
from config import settings

dp = Dispatcher()
bot = Bot(settings.BOT_TOKEN.get_secret_value())