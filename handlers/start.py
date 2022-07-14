import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
👻 ʜᴇʏ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}), ᴀ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs...

ɢᴜɴᴀᴋᴀɴ ᴋᴀᴛᴀ ᴘᴇʀɪɴᴛᴀʜ ʏᴀɴɢ ᴀᴅᴀ ᴅɪᴅᴀʟᴀᴍ ꜱɪɴɪ : ( `/ . • $ ^ ~ + * ?` )
▬▬▬▬▬▬๑۩۩۩۩๑▬▬▬▬▬▬
┣★ʙᴏᴛ ᴍᴜꜱɪᴄ ᴠɪʀᴛᴜᴀʟ 🇮🇩
┣★ᴄʀᴇᴀᴛᴇᴅ ʙʏ ᴘᴜᴛʀᴀ 🇮🇩
╔════════════════════╗
│[🧸 ᴏᴡɴᴇʀ 🧸](t.me/{me})│发 ᴘᴜᴛʀᴀ• 🇮🇩
╚════════════════════╝
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚜️ᴛᴀᴍʙᴀʜᴋᴀɴ ʙᴏᴛ ᴋᴇᴅᴀʟᴀᴍ ɢʀᴜᴘ⚜️", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                   
                      
                    ),
                    InlineKeyboardButton(
                        "🇮🇩 sᴜᴘᴘᴏʀᴛ 🇮🇩", url=f"https://t.me/Grup_Cari_Teman_Virtual"
                    )
                ],[
                   
                    
                    ),
                    InlineKeyboardButton(
                        "👻 ᴄʜᴀɴɴᴇʟ 👻", url=f"https://t.me/PrivateChattingan"
                    )]
            ]
       ),
    )

