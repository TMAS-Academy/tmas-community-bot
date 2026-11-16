"""
Main entry point for the TMAS Academy Community Bot.
"""

import discord
from discord.ext import commands
from tmas_bot.config import DISCORD_TOKEN, GUILD_ID

EXTENSIONS = (
    "tmas_bot.commands.help",
    "tmas_bot.commands.resources",
    "tmas_bot.commands.about",
    "tmas_bot.commands.website",
    "tmas_bot.commands.recommend",
    "tmas_bot.commands.server_info",
    "tmas_bot.commands.rules",
    "tmas_bot.commands.ping",
)

class TMASBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()

        super().__init__(
            command_prefix="!",
            intents=intents,
        )

    async def setup_hook(self):
        """Load extensions and synchronize guild commands."""

        for extension in EXTENSIONS:
            await self.load_extension(extension)

        guild = discord.Object(id=GUILD_ID)

        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

        print("Bot extensions loaded and commands synchronized.")

    async def on_ready(self):
        print(f"Logged in as {self.user}")

bot = TMASBot()

def main():
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()