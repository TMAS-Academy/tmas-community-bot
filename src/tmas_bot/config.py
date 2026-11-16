"""
Configuration management for the TMAS Academy Community Bot.
"""

import os
from dotenv import load_dotenv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

DISCORD_TOKEN = get_required_env("DISCORD_TOKEN")

try:
    GUILD_ID = int(get_required_env("GUILD_ID"))
except ValueError as error:
    raise RuntimeError("GUILD_ID must be a valid integer.") from error