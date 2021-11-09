from AnkiVector.events import register
from AnkiVector import OWNER_ID
from AnkiVector import telethn as tbot
import os 
from PIL import Image, ImageDraw, ImageFont
import shutil 
import random, re
import glob
import time
from telethon.tl.types import InputMessagesFilterPhotos


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/dfc05f886cb635b8e0bdc.jpg", 
                         "https://telegra.ph/file/8f9ff3d743e6707a61489.jpg", 
                         "https://telegra.ph/file/bfc97f4abc4bec6fe860d.jpg", 
                         "https://telegra.ph/file/5ef0f060023600ec08c19.jpg",
                         "https://telegra.ph/file/a448465a3a8a251170f76.jpg",
                         "https://telegra.ph/file/4050e2d89b51373a25d2a.jpg",
                         "https://telegra.ph/file/acbf6038e248e2f64f75a.jpg",
                         "https://telegra.ph/file/6731f80aa9e7ce12d92ec.jpg",
                         "https://telegra.ph/file/f3c9b1564c85057fec402.jpg",
                         "https://telegra.ph/file/d124af16859ab7d5b2342.jpg",
                         "https://telegra.ph/file/50ad4e9c229decba719ad.jpg",
                         "https://telegra.ph/file/86d6242fbcdbb7f3a483a.jpg",
                         "https://telegra.ph/file/4dbe2332fd3419a900b3a.jpg",
                         "https://telegra.ph/file/53d0710d5a1748358ee4c.jpg",
                         "https://telegra.ph/file/2dfcb217a331fa26be864.jpg",
                         "https://telegra.ph/file/b866ce1aca4d42158db0f.jpg",
                         "https://telegra.ph/file/ecdae9c79301064b8e446.jpg"]

@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(random.choice(TELEGRAPH_MEDIA_LINKS))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./AnkiVector/resources/Chopsic.otf", 330)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "AnkiVectorLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Miss_Isabella_Robot ⚡️")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From @isabellasupport , {e}')

@register(pattern="^/biglogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./AnkiVector/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./AnkiVector/resources/Chopsic.otf", 950)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "AnkiVectorLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By  @Miss_Isabella_Robot⚡️")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @isabellasupport, {e}')


@register(pattern="^/wlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./AnkiVector/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "white"
    shadowcolor = "blue"
    font = ImageFont.truetype("./AnkiVector/resources/Maghrib.ttf", 1000)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="white")
    fname2 = "AnkiVectorLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Miss_Isabella_Robot ⚡️ ")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @isabellasupport, {e}')

@register(pattern="^/daalogo ?(.*)")
async def logo_gen(event):
    xx = await eor(event, get_string("com_1"))
    name = event.pattern_match.group(1)
    if not name:
        await eod(xx, "`Give a name too!`")
    bg_, font_ = "", ""
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            if hasattr(temp.media, "document"):
                if "font" in temp.file.mime_type:
                    font_ = await temp.download_media()
                elif (".ttf" in temp.file.name) or (".otf" in temp.file.name):
                    font_ = await temp.download_media()
            elif "pic" in mediainfo(temp.media):
                bg_ = await temp.download_media()
    else:
        pics = []
        async for i in event.client.iter_messages(
            "@UltroidLogos", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
        fpath_ = glob.glob("AnkiVector/resources/*")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in event.client.iter_messages(
            "@UltroidLogos", filter=InputMessagesFilterPhotos
        ):
            pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download_media()
    if not font_:
        fpath_ = glob.glob("AnkiVector/resources/*")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        fnt_size = 150
        strke = 10
    elif len(name) >= 9:
        fnt_size = 50
        strke = 5
    else:
        fnt_size = 130
        strke = 20
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(name, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        name,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text(
        (x, y), name, font=font, fill="white", stroke_width=strke, stroke_fill="black"
    )
    flnme = f"ultd.png"
    img.save(flnme, "png")
    await xx.edit("`Done!`")
    if os.path.exists(flnme):
        await event.client.send_file(
            event.chat_id,
            file=flnme,
            caption=f"Logo by AnkiVector",
            force_document=True,
        )
        os.remove(flnme)
        await xx.delete()
    if os.path.exists(bg_):
        os.remove(bg_)
    if os.path.exists(font_):
        if not font_.startswith("AnkiVector/resources/"):
            os.remove(font_)    
 

@register(pattern="^/redlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./AnkiVector/resources/blackbg.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./AnkiVector/resources/Chopsic.otf", 330)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="red")
    fname2 = "AnkiVectorLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Miss_Isabella_Robot⚡️")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @isabellasupport, {e}')
  

@register(pattern="^/pandalogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./AnkiVector/resources/pandabg.png')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./AnkiVector/resources/font.otf", 170)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "AnkiVectorLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Miss_Isabella_Robot ⚡️")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @isabellasupport, {e}')
   

@register(pattern="^/witchlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./AnkiVector/resources/witch.jpg')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./AnkiVector/resources/font.otf", 170)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "AnkiVectorLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Miss_Isabella_Robot ⚡️")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @isabellasupport, {e}')


@register(pattern="^/spiderlogo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./AnkiVector/resources/spiderbg.png')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./AnkiVector/resources/font.otf", 170)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "AnkiVectorLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Miss_Isabella_Robot⚡️")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From  @isabellasupport, {e}')  
  
  
  
@register(pattern="^/spider_man_logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open('./AnkiVector/resources/spiderbg (2).png')
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 25
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./AnkiVector/resources/font.otf", 170)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "AnkiVectorLogo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @Miss_Isabella_Robot ⚡️")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Go to Help From @isabellasupport, {e}')  
  
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__help__ = """
 ❍ /logo text :  Create your logo with your name
 ❍ /biglogo text :  Create your logo Bigger Than `logo`
 ❍ /wlogo text :
 ❍ /redlogo text :
 ❍ /pandalogo text
 ❍ /spiderlogo text
 ❍ /spider_man_logo text
 """
__mod_name__ = "Logo Maker"
