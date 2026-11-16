"""
Ping command for the TMAS Academy Community Bot.
"""

import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="ping",
        description="Check the bot's connection latency.",
    )
    async def ping(self, interaction: discord.Interaction):
        latency_ms = round(self.bot.latency * 1000)

        embed = discord.Embed(
            title="🏓 Pong!",
            description="The TMAS Academy Community Bot is online.",
            color=discord.Color.green(),
        )

        embed.add_field(
            name="📡 WebSocket Latency",
            value=f"`{latency_ms} ms`",
            inline=True,
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))