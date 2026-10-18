import asyncio
from common import timer

NUMBER_OF_TASKS = 5


async def wait():
    await asyncio.sleep(1)
    print(f"Slept 1 sec")


async def loop_wait():
    tasks = []
    for i in range(NUMBER_OF_TASKS):
        task = asyncio.create_task(wait())
        tasks.append(task)
    for task in tasks:
        await task


@timer
def main():
    asyncio.run(loop_wait())


main()
