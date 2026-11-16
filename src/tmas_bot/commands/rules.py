"""
FileName : rules.py
FileInfo : This file contains the /rules command for the
           TMAS Academy Community Bot.
"""

import discord
from discord import app_commands
from discord.ext import commands

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="rules",
        description="View the TMAS Academy server rules."
    )
    async def rules(self, interaction: discord.Interaction):
        message = (
            "📜 **TMAS Academy Server Rules**\n\n"
            "**1. Be respectful**\n"
            "Be nice to all members and moderators. It is more important "
            "to be kind than to be an IMO qualifier or get all 5s on AP exams.\n\n"

            "**2. Keep it SFW**\n"
            "Keep the chat safe for work. No NSFW.\n\n"

            "**3. No spam**\n"
            "Spamming isn't allowed.\n\n"

            "**4. No cheating**\n"
            "Don't cheat on exams or contests. Don't ask someone to help "
            "you cheat on your test for school. However, we can help you "
            "learn topics to prepare for various exams.\n\n"

            "**5. No advertising**\n"
            "No advertising in this server. Don't DM others to promote something.\n\n"

            "**6. No controversial topics**\n"
            "Do not bring up controversial topics like politics.\n\n"

            "**7. Use common sense**\n"
            "Use common sense and make sure to have fun in this server! 🎉"
        )

        await interaction.response.send_message(message)

async def setup(bot):
    await bot.add_cog(Rules(bot))