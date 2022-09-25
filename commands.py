import datetime

from aiogram import Bot

from config import Config
from funcs import parse_schedule


async def send_schedule(bot: Bot, config: Config):
    lessons = await parse_schedule(date=datetime.datetime.now().isoweekday())
    text = '📚 <b>{date}</b> ga dars jadvali:\n\n' \
           '{lessons}'
    msg = await bot.send_message(
        chat_id=config.tg_bot.group_id,
        text=text.format(
            date=datetime.datetime.now().strftime('%d.%m.%Y'),
            lessons=''.join(lessons)
        )
    )
    await bot.pin_chat_message(
        chat_id=config.tg_bot.group_id,
        message_id=msg.message_id
    )
