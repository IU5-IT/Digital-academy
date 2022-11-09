# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>
import asyncio
from aiogram import Bot, Dispatcher, executor
from config import TOKEN

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handlers import dp, send_to_admin

    executor.start_polling(dp, skip_updates=True, on_startup=send_to_admin)
