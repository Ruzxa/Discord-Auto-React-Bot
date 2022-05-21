import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix='-')
 
@bot.event
async def on_ready():
    print ("Bot Is Ready!")
 
 
@bot.event
async def on_message(message):
    if(message.channel.id == "961699607342121021"):
        await bot.add_reaction(message, "🤍")
 
 
bot.run("OTc3NjI5Mzk3MDYwMjg4NTYy.GFQMa5.fEddM6hBs6KrZQ2GzAQj1jA9Mp8_6JTPgA6tSc")
