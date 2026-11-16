"""
FileName : bot.py
FileInfo : This file contains the main Discord bot setup,
           extension loading, command synchronization, and
           bot startup logic for the TMAS Academy Community Bot.
"""

import discord
from discord.ext import commands
from tmas_bot.config import DISCORD_TOKEN, GUILD_ID

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

async def setup_hook():
    await bot.load_extension("tmas_bot.commands.help")
    await bot.load_extension("tmas_bot.commands.resources")
    await bot.load_extension("tmas_bot.commands.about")
    await bot.load_extension("tmas_bot.commands.website")
    await bot.load_extension("tmas_bot.commands.recommend")
    await bot.load_extension("tmas_bot.commands.server_info")
    await bot.load_extension("tmas_bot.commands.rules")
    await bot.load_extension("tmas_bot.commands.ping")

    guild = discord.Object(id=GUILD_ID)

    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)

bot.setup_hook = setup_hook

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(DISCORD_TOKEN)