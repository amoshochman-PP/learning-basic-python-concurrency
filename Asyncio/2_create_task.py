import asyncio
from common import timer, TASKS_NUM

async def asyncio_wait():
    await asyncio.sleep(1)
    print(f"Slept 1 sec")

async def loop_wait():
    tasks = []
    for i in range(TASKS_NUM):
        task = asyncio.create_task(asyncio_wait())
        tasks.append(task)
    for task in tasks:
        await task


@timer
def main():
    asyncio.run(loop_wait())


main()
