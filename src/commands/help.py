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
        message = (
            "📚 **TMAS Academy Community Bot**\n\n"
            "Here are the available commands:\n\n"
            "`/help` — View this help message\n"
            "`/resources` — Browse TMAS Academy STEM resources\n"
            "`/recommend` — Get a STEM book recommendation\n"
            "`/about` — Learn more about TMAS Academy\n"
            "`/website` — Visit the TMAS Academy website\n"
            "`/server_info` — View basic information about the TMAS Academy server\n"
            "`/rules` — View the TMAS Academy server rules\n"
            "`/ping` — Check if the TMAS Academy Community Bot is online"
        )
        
        await interaction.response.send_message(message)

async def setup(bot):
    await bot.add_cog(Help(bot))