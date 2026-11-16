"""
Server information command for the TMAS Academy Community Bot.
"""

import discord
from discord import app_commands
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name="server_info",
        description="View basic information about the TMAS Academy server.",
    )
    async def server_info(self, interaction: discord.Interaction):
        guild = interaction.guild

        if guild is None:
            await interaction.response.send_message(
                "This command can only be used inside a server.",
                ephemeral=True,
            )
            return

        embed = discord.Embed(
            title=f"🏠 {guild.name}",
            color=discord.Color.blue(),
            timestamp=guild.created_at,
        )

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(
            name="👥 Members",
            value=f"{guild.member_count:,}",
            inline=True,
        )

        embed.add_field(
            name="🆔 Server ID",
            value=f"`{guild.id}`",
            inline=True,
        )

        embed.add_field(
            name="📅 Created",
            value=discord.utils.format_dt(guild.created_at, style="D"),
            inline=False,
        )

        embed.set_footer(text="TMAS Academy Community")

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(ServerInfo(bot))