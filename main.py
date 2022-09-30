import discord
from discord.ext import commands
bot=discord.Client(command_prefix="g")

@bot.command()
async def wew(ctx):
    await ctx.send(".")
bot.run(TOKEN)