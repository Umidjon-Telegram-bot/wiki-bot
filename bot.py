import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5588298392:AAH4-1CGsWIzHYotRE2ZiCbuid6Opcv-iwM'

wikipedia.set_lang("uz")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(f"Assalomu alaykum. {message.chat.full_name} Wikipedia botiga xush kelibsiz!")

@dp.message_handler()
async def sendWiki(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        msg = wikipedia.summary(message.text)
        await message.answer(msg)
    except:
        await  message.answer(f'Xurmatli {message.chat.first_name} Bizda bunday maqola topilmadi!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)