# https://www.youtube.com/@PythonHubStudio
import os
import logging

from dotenv import find_dotenv, load_dotenv

import asyncio
from aiogram import Bot, Dispatcher, types

from handlers.user_private import user_private_router
from common.bot_cmds_list import private


logging.basicConfig(level=logging.INFO)
load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message', 'edited_message' ]

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats()) # Створюємо меню
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats()) Удалить меню
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())