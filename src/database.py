"""
FileName : database.py
FileInfo : This file contains the database connection logic for
           the TMAS Academy Community Bot.
"""

import asyncpg
from config import DATABASE_URL
_pool = None

async def initialize_database():
    global _pool
    _pool = await asyncpg.create_pool(DATABASE_URL)

def get_pool():
    return _pool