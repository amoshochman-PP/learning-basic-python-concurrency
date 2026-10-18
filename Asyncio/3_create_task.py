import asyncio
from common import timer

NUMBER_OF_TASKS = 5


async def wait():
    print(f"Sleeping 1 second")
    await asyncio.sleep(1)


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
