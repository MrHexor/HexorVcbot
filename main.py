import asyncio
from pytgcalls import idle
from driver.veez import call_py, bot

bot.start()
call_py.start()
idle()
