"""This is the module with main logic"""

from data_parsing.parse_amount import DataParser, DBManager


class DataGetter:
    def __init__(self):
        self._manager = DBManager()
        self._parser = DataParser()

    async def get_amount(self) -> None:
        current_amount = await self._parser.get_amount()
        max_value = await self._manager.max_amount_per_hour()
        one_percent = max_value / 100
        if (max_value - current_amount) >= one_percent:
            print('Цена упала на 1% от максимальной цены за последний час!')
        else:
            print('works')
