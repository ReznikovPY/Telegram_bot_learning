from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.enums import ParseMode
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from filters.chat_types import ChatTypeFilter

from PythonHubStudio.keyboards import reply
from pydantic import BaseModel, ConfigDict

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


# @user_private_router.message(CommandStart())
# async def start_cmd(message: types.Message):
#     await message.answer("Привіт, я віртуальний помічник", reply_markup=reply.test_kb)

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привіт, я віртуальний помічник",
                         reply_markup=reply.start_kb3.as_markup(
                             resize_keyboard=True,
                             input_field_placeholder='Що Вас цікавить?'))

# @user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(or_f(Command("menu"), (F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer("Ось меню:")
# В await message.answer("Ось меню:") можна передати нову клавіатуру
# або видалити клавіатуруб передаємо reply_markup=reply.del_kbd
#------------------------------------------




@user_private_router.message(F.text.lower() == "наші послуги")
@user_private_router.message(Command("services"))
async def about_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold('Наші послуги'),
            'Манікюр',
            'Педікюр',
            'Стрижка',
            marker='✅'
        ),
        as_marked_section(
            Bold('Не надаємо:'),
            'Епіляція ануса',
            'Ремонт тостерів',
            marker='❌'
        ),
        sep='\n-------------\n'
    )
    await message.answer(text.as_html())


@user_private_router.message(F.text.lower() == "варіанти оплати")
@user_private_router.message(Command("payment"))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        Bold('Варіанти оплати:'),
        'Грошима',
        'Бухлом',
        'Мертвими москалями',
        marker='👉'
    )
    await message.answer(text.as_html())


# @user_private_router.message(F.text.lower() == "Ваші дані")
# @user_private_router.message(Command("your_data"))
# async def get_contact(message: types.Message):
#     await message.answer("Your data",
#                          reply_markup=reply.test_kb)

# @user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варіанти доставки'))
# @user_private_router.message(Command("shipping"))
# async def menu_cmd(message: types.Message):
#     text = as_list(
#         as_marked_section(
#             Bold('Варіанти доставки:🚚'),
#             'Курєр',
#             'Самовивіз',
#             'Нова пошта',
#             marker='✅'
#         ),
#         as_marked_section(
#             Bold('Не дсставляємо:'),
#             'Укр пошта',
#             'Голуби',
#             marker='❌'
#         ),
#         sep='\n-------------\n'
#     )
#     await message.answer(text.as_html())


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f'Контакт отриманий')
    await message.answer(F.contact.phone_number)

@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f'локація отриманий')
    await message.answer(F.location)


# @user_private_router.message(F.content_type == ContentType.CONTACT)
# async def handle_contact(message: types.Message):
#     phone_number = message.contact.phone_number
#     await message.answer(F.user.id, phone_number)

# https://www.instagram.com/my_crazy_house_/