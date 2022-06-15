# (c) @AbirHasan2005

from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database
from pyrogram.types import User

@Client.on_message(filters.command(["start"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar 🤔")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="Hi,{message.from_user.mention}!\n\n"
             "I can rename media without downloading it!\n"
             "Speed depends on your media DC.\n\n"
             "Just send me media and reply to it with /rename command.",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("Updates", url="https://t.me/Desi_iBoTs"),
           types.InlineKeyboardButton("Updates", url="https://t.me/Desi_iBoTs")
        ]])
    )

@Client.on_message(filters.command("settings") & filters.private & ~filters.edited)
async def settings_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar 🤔")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="Here you can setup your settings....!",
        reply_markup=types.InlineKeyboardMarkup(
            [[types.InlineKeyboardButton("Show Settings", callback_data="showSettings")]]
        ),
        disable_web_page_preview=True,
        reply_to_message_id=m.message_id
    )
