import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9ab995651c8c610010fcf.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
🔱 ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣❥︎ ᴄʀᴇᴀᴛᴏʀ : [ʟᴜᴄɪғᴇʀ](https://t.me/@LUCYY_xZz)
┣❥︎ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : [ᴊᴏɪɴ](https://t.me/luxclub_sergio)
┗━━━━━━━━━━━━━━━━━┛

🩸 ᴅᴏɴᴛ ᴅᴍ ᴍᴇ ᴡɪᴛʜᴏᴜᴛ ᴘᴇʀᴍɪssɪᴏɴ
ᴅᴍ ᴛᴏ ᴍʏ [ᴘᴀᴘᴀ](https://t.me/@LUCYY_xZz)
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔱 ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🔱", url=f"https://t.me/luxclub_sergio")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9ab995651c8c610010fcf.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴊᴏɪɴ ɴᴏᴡ", url=f"https://t.me/luxclub_sergio")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9ab995651c8c610010fcf.jpg",
        caption=f"""𝐏𝐑𝐈𝐕𝐀𝐓𝐄 𝐑𝐄𝐌𝐏𝐎""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴘʀɪᴠᴀᴛᴇ ʀᴇᴍᴘᴏ", url=f"ɴᴏᴛʜɪɴɢ ʜᴇʀᴇ")
                ]
            ]
        ),
    )
