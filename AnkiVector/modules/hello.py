from AnkiVector.decorator import register
from .utils.disable import disableable_dec
from .utils.message import get_args_str

@register(cmds="Alexie")
@disableable_dec("Alexie")
async def _(message):
    j = "Hello there my name is Alexie"
    await message.reply(j)
    

__help__ = """
<b>Hi</b>
- /hi: Hello there my name is Alexie
"""
__mod_name__ = "Alexie"
