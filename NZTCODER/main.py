# https://www.youtube.com/@nztcoder
from aiogram import Bot, Dispatcher
import asyncio
import logging

from handlers.basic import get_start
from settings import settings

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот запущено!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот зупинено')


async def start():
    logging.basicConfig(
        level=logging.INFO,  # Встановлює рівень логування на рівень INFO.
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(filename)s.%(funcName)s(%(lineno)d) - %(message)s"
        # Визначає формат повідомлень журналу.
    )

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())