"""
FileName : website.py
FileInfo : This file contains the /website command for providing
           a link to the TMAS Academy website.
"""

import discord
from discord import app_commands
from discord.ext import commands

class Website(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="website",
        description="Visit the TMAS Academy website."
    )
    async def website(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "Visit the TMAS Academy website: https://tmasacademy.github.io/"
        )

async def setup(bot):
    await bot.add_cog(Website(bot))