"""This module works with DB data"""

import asyncio

from datetime import datetime, timedelta
from decimal import Decimal
from database.connection import Connection


class DBManager:
    def __init__(self):
        self._connection = Connection()

    async def create_record(self, amount: Decimal) -> bool:
        command = (
            "INSERT INTO test_table(datetime, amount) VALUES ($1, $2)"
        )
        try:
            async with self._connection as conn:
                await conn.execute(command, datetime.now(), amount)
            return True
        except Exception as e:
            print(e)
            return False

    async def max_amount_per_hour(self) -> Decimal:
        start_time = datetime.now() - timedelta(minutes=60)
        finish_time = datetime.now()
        command = (
            "SELECT amount FROM test_table WHERE datetime < $1 AND datetime > $2"
        )
        async with self._connection as conn:
            res_list = await conn.fetch(command, finish_time, start_time)
        return (max(res_list))[0]
