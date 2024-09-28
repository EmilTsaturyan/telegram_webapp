from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart

from core import settings
from .inline import inline_builder



bot = Bot(settings.telegram_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    text = ('👽 Welcome to the world of BeamBot 🚀\n\n'
            'Calling all humanoids, the depths of space are yours to fight for, set to the tune of cryptocurrency and special missions... 🌒\n'
            'As an ambitious galactic explorer, you find yourself on the verge of riches and wealth, where collecting crystals and coins will line your pockets with the most expensive space dust... 🌌'
            )
    
    photo = FSInputFile('bot/images/start.jpg')
    await bot.send_photo(message.chat.id, photo=photo, caption=text, reply_markup=inline_builder(settings.webapp_url, message.chat.id))

