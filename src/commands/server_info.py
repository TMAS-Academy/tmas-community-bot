"""
FileName : server_info.py
FileInfo : This file contains the /server-info command for the
           TMAS Academy Community Bot.
"""

import discord
from discord import app_commands
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="server_info",
        description="View basic information about the TMAS Academy server."
    )
    async def server_info(self, interaction: discord.Interaction):
        message = (
            f"🏠 **{interaction.guild.name}**\n\n"
            f"👥 Members: {interaction.guild.member_count}\n"
            f"📅 Created: {interaction.guild.created_at}"
        )

        await interaction.response.send_message(message)

async def setup(bot):
    await bot.add_cog(ServerInfo(bot))