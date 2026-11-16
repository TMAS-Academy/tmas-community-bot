"""
Resource finder command for TMAS Academy.
"""

import discord
from discord import app_commands
from discord.ext import commands

WEBSITE_URL = "https://www.tmasacademy.com/"
BOOKS_URL = "https://www.tmasacademy.com/books"

class Resources(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="resources",
        description="Explore free TMAS Academy STEM resources.",
    )
    async def resources(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📚 TMAS Academy Resource Center",
            description=(
                "Looking for study materials? Explore our free "
                "STEM educational resources!"
            ),
            color=discord.Color.blue(),
            url=BOOKS_URL,
        )

        embed.add_field(
            name="📖 TMAS Book Library",
            value=(
                "Explore our collection of free STEM study guides "
                "and educational books.\n"
                f"[Browse All Books]({BOOKS_URL})"
            ),
            inline=False,
        )

        embed.add_field(
            name="🌐 TMAS Academy Website",
            value=(
                "Learn more about TMAS Academy and our educational "
                "initiatives.\n"
                f"[Visit TMAS Academy]({WEBSITE_URL})"
            ),
            inline=False,
        )

        embed.set_footer(
            text="TMAS Academy • Free STEM Education for Everyone"
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Resources(bot))