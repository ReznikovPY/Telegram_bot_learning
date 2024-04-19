from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import emoji


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="Наші послуги"),
        ],
        {
            KeyboardButton(text="Варіанти оплати"),
            KeyboardButton(text="Ваші дані"),
        }
    ],
    resize_keyboard=True,
    input_field_placeholder='Что Вас интересует?'
)

del_kbd = ReplyKeyboardRemove()

# Інший віріант створення клавіатури
start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Меню"),
    KeyboardButton(text="Наші послуги"),
    KeyboardButton(text="Варіанти оплати"),
    KeyboardButton(text="Ваші дані"),
)
# Вказуємо скільки кнопок іде в ряду
start_kb2.adjust(2, 2)

# Якщо в клівіатуру потрібно добавить ще кнопку, можна зробити це так
start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text="Надіслати номер ☎️", request_contact=True),
              KeyboardButton(text="Надіслати локацію 🗺️", request_location=True)
              )


# data_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Перадати дані', request_contact=True)
#             # KeyboardButton(text="Створити опитування ❓", request_poll=KeyboardButtonPollType()),
#         ],
#     ],
#     resize_keyboard=True,
# )


test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Створити опитування ❓", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Надіслати номер ☎️", request_contact=True),
            KeyboardButton(text="Надіслати локацію 🗺️", request_location=True),
        ],
    ],
    resize_keyboard=True,
)
