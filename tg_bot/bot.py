import asyncio
from loader import bot, dp
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiohttp import ClientSession
from datetime import datetime


@dp.message(Command('messages'))
async def get_messages(message: Message):
    async with ClientSession() as session:
        async with await session.get('http://web:8000/api/v1/messages') as response:
            all_messages = await response.json()
    if isinstance(all_messages, list):
        answer_string = '\n'
        for user_message in all_messages:
            answer_string += f'Пользователь: {user_message["user"]}\nСообщения: {", ".join(user_message["messages"])}\n\n'
        await message.answer(answer_string)
    else:
        await message.answer('Сообщений нет')


@dp.message(F.text)
async def text_message(message: Message):
    if message.text:
        async with ClientSession() as session:
            await session.post('http://web:8000/api/v1/message', json={"user": int(message.from_user.id), "message": str(message.text)})
        await message.answer('Сообщение записано')
    else:
        await message.answer('Пришлите текстовое сообщение')


async def main():
    await bot.send_message(539937958, 'Бот запущен')
    await dp.start_polling(bot)


asyncio.run(main())