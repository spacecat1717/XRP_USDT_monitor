"""This module parses data and return current value"""

import asyncio
import httpx

from decimal import Decimal
from bs4 import BeautifulSoup as bs

from database.manager import DBManager


"""I know using API is a better way, but I couldn't get the API key, so it's html scraping"""


class DataParser:
    def __init__(self):
        self._manager = DBManager()
        self._url = 'https://www.binance.com/ru/futures/XRPUSDT'
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0'
        }

    async def get_amount(self) -> bool:
        amount = await self._parse_amount()
        res = await self._save_amount(amount)
        return res

    async def _parse_amount(self) -> Decimal:
        async with httpx.AsyncClient(trust_env=True, headers=self._headers) as client:
            response = await client.get(url=self._url)
        page_data = (bs(response.text, 'lxml').text).split()
        res = Decimal(page_data[0])
        return res

    async def _save_amount(self, amount: Decimal) -> bool:
        if await self._manager.create_record(amount):
            return True
        return False

