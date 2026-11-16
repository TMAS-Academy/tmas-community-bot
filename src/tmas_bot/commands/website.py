"""
Website command for TMAS Academy.
"""

import discord
from discord import app_commands
from discord.ext import commands

WEBSITE_URL = "https://www.tmasacademy.com/"

class Website(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="website",
        description="Visit the TMAS Academy website.",
    )
    async def website(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🌐 TMAS Academy Website",
            description=(
                "Explore TMAS Academy and discover our free "
                "educational resources."
            ),
            url=WEBSITE_URL,
            color=discord.Color.blue(),
        )

        embed.add_field(
            name="Visit Us",
            value=f"[www.tmasacademy.com]({WEBSITE_URL})",
            inline=False,
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Website(bot))