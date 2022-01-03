"""
MIT License

Copyright (c) 2021 Tinura Dinith

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from functools import wraps
from AnkiVector import pbot as bolt
from pyrogram import filters
from AnkiVector.utils.sql.antichnl_sql import is_antichannel, antichanl_on, antichanl_off

def is_admin(func):
    @wraps(func)
    async def oops(client,message):
        is_admin = False
        try:
            user = await message.chat.get_member(message.from_user.id)
            admin_strings = ("creator", "administrator")
            if user.status not in admin_strings:
                is_admin = False
            else:
                is_admin = True

        except ValueError:
            is_admin = True
        if is_admin:
            await func(client,message)
        else:
            await message.reply("ඇඩ්මින්ලට විතරයි මේක ඔන් කරන්න පුලුවන්!")
    return oops

@bolt.on_message(filters.command("antichannel"))
@is_admin
async def antich_toggle(_, message):
    if len(message.command) < 2:
        return await message.reply_text("/antichannel සමග On හෝ Off භාවිතා කරන්න")
    status = message.text.split(None, 1)[1].strip()
    status = status.lower()
    chat_id = message.chat.id
    if status == "on":
        if (is_antichannel(message.chat.id)):
            return await message.reply("දැනටමත් ක්‍රියාත්මක කර ඇත")
        else:
         antichanl_on(chat_id)
         await message.reply_text("Antichannel සබල කර ඇත.")
    elif status == "off":
        if not (is_antichannel(str(message.chat.id))):
            return await message.reply("දැනටමත් අක්රිය කර ඇත")
        else:
         antichanl_off(chat_id)
         await message.reply_text("Antichannel අබල කර ඇත.")
    else:
        await message.reply_text("/antichannel සමග On හෝ Off භාවිතා කරන්න")

@bolt.on_message(filters.incoming & ~filters.linked_channel, group=6)
async def anitchnlmg(_, message):
  if message.sender_chat:
    if (is_antichannel(message.chat.id)):
      await message.delete() 
    else:
        return


__name__ = "Anti-Channel 📣"
__help__ = """
• /antichannel `on/off` - Antichannel සක්‍රිය සහ අක්‍රිය කිරීමට
"""
