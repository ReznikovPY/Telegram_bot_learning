from string import punctuation

from aiogram import Router, types, F


user_group_router = Router()

restricted_words = {'дура', 'курица', 'лайно'}

# перевіряє правописання, щоб не могли замаскувати лайку
def clean_teaxt(text:str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.message()
async def words_cleaner(message: types.Message):
    if restricted_words.intersection(message.text.lower().split()):
        await message.answer(f'{message.from_user.first_name}, еди себе достойно!!!')
        await message.delete()
        # await message.chat.ban(message.from_user.id)