import asyncio

from multiprocessing import Process

from database.create import CreateTable
from scheduled_task.scheduler import run, scheduler

if __name__ == "__main__":
    table = CreateTable()
    asyncio.run(table.create_table())
    asyncio.run(scheduler())


