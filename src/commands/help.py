"""
FileName : help.py
FileInfo : This file contains the /help command for the
           TMAS Academy Community Bot.
"""

import discord
from discord import app_commands
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="help",
        description="View the available TMAS Academy commands."
    )
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "TMAS Academy Community Bot commands coming soon!"
        )

async def setup(bot):
    await bot.add_cog(Help(bot))