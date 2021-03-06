# (c) @AbirHasan2005

from configs import Config
from .database import db
from pyrogram import Client
from pyrogram.types import Message


async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_flooded_message(
                int(Config.LOG_CHANNEL),
                f"#ššš°_šš¬šš« \n\nā® ššš¦š - {cmd.from_user.first_name} \nā® šš - <code>{cmd.from_user.id}</code> \nā® started @{(await bot.get_me()).username}"
            )
