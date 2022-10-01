import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()
bot_token=os.getenv('TOKEN1')+os.getenV('TOKEN2')
bot=discord.Client(command_prefix="g")

@bot.command()
async def wew(ctx):
    await ctx.send(".")
bot.run(bot_token)
