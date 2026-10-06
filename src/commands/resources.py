"""
FileName : resources.py
FileInfo : This file contains the /resources command for
           browsing TMAS Academy STEM resources.
"""

import discord
from discord import app_commands
from discord.ext import commands

class Resources(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="resources",
        description="Browse TMAS Academy STEM resources."
    )
    async def resources(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "TMAS Academy resources coming soon!"
        )

async def setup(bot):
    await bot.add_cog(Resources(bot))