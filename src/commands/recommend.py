"""
FileName : recommend.py
FileInfo : This file contains the /recommend command for
           providing STEM book recommendations.
"""

import discord
from discord import app_commands
from discord.ext import commands

class Recommend(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="recommend",
        description="Get a STEM book recommendation."
    )
    async def recommend(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "The TMAS book recommendation system is coming soon!"
        )

async def setup(bot):
    await bot.add_cog(Recommend(bot))