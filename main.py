import asyncio


from database.create import CreateTable
from scheduled_task.scheduler import run

if __name__ == "__main__":
    table = CreateTable()
    asyncio.run(table.create_table())
    asyncio.run(run())


