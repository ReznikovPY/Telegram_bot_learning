from aiogram import Bot
from aiogram.types import Message

async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привіт {message.from_user.first_name}. Радий тебе бачити')
    # await bot.send_message(message.from_user.id, f'Привіт {message.from_user.first_name}. Радий тебе бачити')

# Збереження надсилаємих зображень
async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Ти відправив картинку! я збережу її собі')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')
