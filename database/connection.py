"""this module creates connection to DB using Singleton class"""

import asyncpg


class Connection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Connection, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):

        if (self.__initialized):
            return
        self.__initialized = True
        self._db_name = 'test_1'
        self._db_user = 'postgres'
        self._db_password ='Teatea_0'
        self._db_host = 'localhost'
        self._conn = None

    async def _get_conn(self):
        return self._conn

    conn = property(_get_conn)

    async def __aenter__(self):
        self._conn = await asyncpg.connect(database=self._db_name, user=self._db_user, password=self._db_password,
                                           host=self._db_host)
        return self._conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._conn.close()