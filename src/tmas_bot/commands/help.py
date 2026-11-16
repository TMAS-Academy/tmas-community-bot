"""
Help command for the TMAS Academy Community Bot.
"""

import discord
from discord import app_commands
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="help",
        description="View the available TMAS Academy commands.",
    )
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="🤖 TMAS Academy Community Bot",
            description=(
                "Here are the commands available to help you "
                "navigate the TMAS Academy community."
            ),
            color=discord.Color.blue(),
        )

        embed.add_field(
            name="📚 Educational Resources",
            value=(
                "`/resources` — Browse TMAS Academy books and resources.\n"
                "`/recommend` — Find a book based on your course or topic."
            ),
            inline=False,
        )

        embed.add_field(
            name="🏠 Community Information",
            value=(
                "`/about` — Learn about TMAS Academy.\n"
                "`/website` — Visit the TMAS Academy website.\n"
                "`/rules` — Review the community rules.\n"
                "`/server_info` — View server information."
            ),
            inline=False,
        )

        embed.add_field(
            name="🛠️ Utilities",
            value="`/ping` — Check bot connectivity and latency.",
            inline=False,
        )

        embed.set_footer(
            text="TMAS Academy • Free STEM Education for Everyone"
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Help(bot))