"""This module creates table. It runs within main.py file"""

import asyncio

from database.connection import Connection


class CreateTable:
    def __init__(self):
        self._connection = Connection()

    async def create_table(self) -> bool:
        command = (
            "CREATE TABLE IF NOT EXISTS test_table(\
            id SERIAL,\
            datetime TIMESTAMP,\
            amount DECIMAL\
            )"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command)
            return True
        except Exception as e:
            print(e)
            return False




