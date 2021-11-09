import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/e1ff8620519d6378ac1f0.jpg) To Make Your Groups Secured And Organized !** \n\n**『 Owner 』 : 『 [Kyy](t.me/IDnyaKosog) 』**\n**╭──────────────**\n**┣─ » Python ~ 3.8.6**\n**┣─ » Update ~ Recently**\n**╰──────────────**\n\n**»» 『 @ahhsudahlahhh 』 ««**"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ʀᴇᴘᴏ", url=f"https://github.com/muhammadrizky16"),
        InlineKeyboardButton("ᴊᴏɪɴ", url=f"https://t.me/FlicksSupport"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/IDnyaKosong"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/FlicksSupport"),
      ],[
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/ahhsudahlahhh"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/devoloperflicks/32"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
