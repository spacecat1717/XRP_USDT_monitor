"""This module works with aioschedule to do periodic tasks"""

import asyncio
import aioschedule

from get_data.get_data import DataGetter


async def scheduler() -> None:
    get_data = DataGetter()
    aioschedule.every(5).seconds.do(get_data.get_amount)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(5)





