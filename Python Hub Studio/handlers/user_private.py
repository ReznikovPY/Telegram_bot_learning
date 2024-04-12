from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command,or_f

from aiogram.types import ContentType

user_private_router = Router()


# Хэндлер на команду /start
@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привіт, я віртуальний помічник')


#
# @user_private_router.message(F.text.lower() == 'меню')
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
async def menu_cmd(message: types.Message):
    await message.answer('Ось меню:')


@user_private_router.message(Command('about'))
async def description(message: types.Message):
    await message.answer('Опис:')


# Можна один хендлер вішати поверх іншого, також в магічних фільтрах можна обєднувати умови
@user_private_router.message((F.text.lower().contains('знаходит')) | (F.text.lower() == 'адреса'))
@user_private_router.message(Command('contacts'))
async def another_description(message: types.Message):
    await message.answer('Тел: +380** *** ** **')


# @user_private_router.message(F.content_type == ContentType.CONTACT)
# async def handle_contact(message: types.Message):
#     phone_number = message.contact.phone_number
#     await message.answer(F.user.id, phone_number)