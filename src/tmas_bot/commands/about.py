"""
About command for TMAS Academy.
"""

import discord
from discord import app_commands
from discord.ext import commands

WEBSITE_URL = "https://www.tmasacademy.com/"

class About(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="about",
        description="Learn more about TMAS Academy.",
    )
    async def about(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="📚 About TMAS Academy",
            description=(
                "TMAS Academy is a nonprofit organization dedicated "
                "to providing high-quality, free educational resources "
                "to students."
            ),
            color=discord.Color.blue(),
            url=WEBSITE_URL,
        )

        embed.add_field(
            name="Our Mission",
            value=(
                "Making quality STEM education and learning resources "
                "accessible to students."
            ),
            inline=False,
        )

        embed.add_field(
            name="🌐 Learn More",
            value=f"[Visit TMAS Academy]({WEBSITE_URL})",
            inline=False,
        )

        embed.set_footer(text="Free STEM Education for Everyone")

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))