# Copyright © 2022 mightyK1ngRichard <dimapermyakov55@gmail.com>

from main import bot, dp
from aiogram.types import Message
from config import admin_id


async def send_to_admin():
    await bot.send_message(chat_id=admin_id, text='Бот запущен')


@dp.message_handler()
async def echo(message: Message):
    text = ''
    await bot.send_message(message.from_user, text=text)
    await message.answer(text=text)
