from string import punctuation

from aiogram import F, types, Router

from PythonHubStudio.filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))
user_group_router.edited_message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {'дура', 'курица', 'лайно', 'овца'}

# перевіряє правописання, щоб не могли замаскувати лайку
def clean_teaxt(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f'А-та-тат {message.from_user.first_name}, веди себе культурно!!!')
        await message.delete()
        # await message.chat.ban(message.from_user.id)