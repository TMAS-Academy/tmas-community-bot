"""
Resource finder command for TMAS Academy.
"""

import discord
from discord import app_commands
from discord.ext import commands

class Resources(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="resources",
        description="Explore free TMAS Academy STEM resources."
    )
    async def resources(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📚 TMAS Academy Resource Center",
            description=(
                "Looking for study materials? Explore our free "
                "STEM educational resources!"
            ),
            color=discord.Color.blue(),
            url="https://www.tmasacademy.com/resources"
        )

        embed.add_field(
            name="📖 STEM Study Guides",
            value=(
                "Explore free study guides covering AP courses, "
                "competitive mathematics, and more.\n"
                "[Browse Study Guides]"
                "(https://www.tmasacademy.com/resources)"
            ),
            inline=False
        )

        embed.add_field(
            name="📚 TMAS Book Library",
            value=(
                "Browse the collection of TMAS Academy books "
                "and educational materials.\n"
                "[Explore Books]"
                "(https://www.tmasacademy.com/books)"
            ),
            inline=False
        )

        embed.add_field(
            name="🌐 TMAS Academy Website",
            value=(
                "Discover more about our organization, resources, "
                "and educational initiatives.\n"
                "[Visit TMAS Academy]"
                "(https://www.tmasacademy.com/)"
            ),
            inline=False
        )

        embed.set_footer(
            text="TMAS Academy • Free STEM Education for Everyone"
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Resources(bot))