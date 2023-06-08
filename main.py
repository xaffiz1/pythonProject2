from aiogram import Bot, Dispatcher, types, executor
import logging
import os

API_TOKEN = os.environ['TOKEN']
# API_TOKEN = '5801589511:AAGflay4aVNi2jpWJZlIBlkIL7YKQa_EKmc'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def initual_handler(msg:types.Message):
    await msg.answer('Xush kelibsiz')

@dp.message_handler()
async def handle_msg(msg: types.Message):
    print(msg.text)
    text = msg.text.lower()
    count = sum(text.count(vowel) for vowel in 'aeiou')

    if count > 5:
        await msg.delete()
        await msg.answer("5 ta dan ko'p unli xarf bor")




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)