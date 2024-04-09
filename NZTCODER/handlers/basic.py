from aiogram import Bot
from aiogram.types import Message

async def get_start(message: Message, bot: Bot):
    # await bot.send_message(message.from_user.id, f'Привіт {message.from_user.first_name}. Радий тебе бачити')
    await message.answer(f'Привіт {message.from_user.first_name}. Радий тебе бачити')