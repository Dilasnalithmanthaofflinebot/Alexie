import re
from  import pbot as sz
from io import BytesIO
from requests import get
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os 
from PIL import Image, ImageDraw, ImageFont
import random
import requests
import shutil




def nospace(s):

    s = re.sub(r"\s+", '%20', s)

    return s
@sz.on_message(filters.command(["write", f"write@miss_Alexie_bot"]))
async def make_logo(_, message):
    imgcaption = f"""
☘️** Write Successfully**✅
◇───────────────◇
🔥 **Created by** : @miss_Alexie_bot
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : `Sl Ninja Team`
◇───────────────◇
**All Right Reserved**⚠️️
"""
    if len(message.command) < 2:
            return await message.reply_text("Please give a text to Write")
    m = await message.reply_text("📸 Creating..")
    name = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
    api = get(f"https://single-developers.herokuapp.com?write={name}")
    await m.edit("📤 Uploading ...")
    await sz.send_chat_action(message.chat.id, "upload_photo")
    img = Image.open(BytesIO(api.content))
    logoname = "szlogo.png"
    img.save(logoname, "png")
    await message.reply_photo(photo = logoname,
                              caption=imgcaption,)
    await m.delete()
    if os.path.exists(logoname):
            os.remove(logoname)
            
__help__ = """
 • /write <text> :  Write To Your Text
 """
__mod_name__ = "Hand Write✍️"
