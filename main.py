import logging
from asyncio import get_event_loop
import reddit
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import WrongFileIdentifier, BadRequest

API_TOKEN = 'XXXXXXXXXXXXX'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, loop=get_event_loop())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Запущен.")
    await scheduled(3)


async def scheduled(wait_for):
    while True:
        # await asyncio.sleep(wait_for)
        await reddit.obnov()
        await reddit.sravn()
        await sendAttachment(reddit.dot, reddit.dot1)


async def sendAttachment(type1: str, type2: str):
    reddit.zapis()
    if (type1 == '.') or (type2 == '.'):
        if type == "gif":
            try:
                try:
                    await bot.send_video(
                        chat_id='Channel_ID',
                        video=reddit.submission.url,
                        caption=reddit.title,
                        parse_mode='HTML',
                        disable_notification=True)
                except WrongFileIdentifier:
                    pass
            except BadRequest:
                pass
        else:
            try:
                try:
                    await bot.send_photo(
                        chat_id='-Channel_ID',
                        photo=reddit.submission.url,
                        caption=reddit.title,
                        parse_mode="HTML",
                        disable_notification=True)
                except WrongFileIdentifier:
                    pass
            except BadRequest:
                pass
    else:
        await scheduled(10)


if __name__ == '__main__':
    dp.loop.create_task(scheduled(60))
    executor.start_polling(dp, skip_updates=True)
