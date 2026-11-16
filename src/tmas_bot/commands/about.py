"""
FileName : about.py
FileInfo : This file contains the /about command for providing
           information about TMAS Academy.
"""

import discord
from discord import app_commands
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="about",
        description="Learn more about TMAS Academy."
    )
    async def about(self, interaction: discord.Interaction):
        message = (
            "📚 **TMAS Academy**\n\n"
            "TMAS Academy is a nonprofit organization dedicated to providing "
            "high-quality, free educational resources to students worldwide."
        )

        await interaction.response.send_message(message)

async def setup(bot):
    await bot.add_cog(About(bot))