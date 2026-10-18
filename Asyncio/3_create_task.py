import asyncio
from common import timer, TASKS_NUM, async_wait


async def loop_wait():
    tasks = []
    for i in range(TASKS_NUM):
        task = asyncio.create_task(async_wait())
        tasks.append(task)
    for task in tasks:
        await task


@timer
def main():
    asyncio.run(loop_wait())


main()
