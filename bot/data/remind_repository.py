import aiosqlite
from discord import guild
import discord

from bot.data.base_repository import BaseRepository

class RemindRepository(BaseRepository):

    async def insert_reminder(self, id, user: discord.user.id, message: str, time):
        async with aiosqlite.connect(self.resolved_db_path) as db:
            await db.execute(
                """
                INSERT INTO Remind (id, user, message, time) 
                VALUES (?, ?, ?, ?, ?)
                """, (id, user, message, time))
            await db.commit()
    
    async def delete_reminder(self, id):
        async with aiosqlite.connect(self.resolved_db_path) as db:
            await db.execute(
                """
                DELETE FROM Remind WHERE id = ?
                """, id)
            await db.commit()
    
    async def get_tag(self, id: discord.user.id) -> str:
        async with aiosqlite.connect(self.resolved_db_path) as db:
            async with db.execute('SELECT * FROM Remind WHERE id = ?',
                    (id)) as c:
                return await self.fetcthone_as_dict(c)

