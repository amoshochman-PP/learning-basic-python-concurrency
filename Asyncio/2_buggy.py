import asyncio
from common import timer, asyncio_wait, TASKS_NUM


async def loop_wait():
    for i in range(TASKS_NUM):
        await asyncio_wait()
        # asyncio.create_task(async_wait())


@timer
def main():
    asyncio.run(loop_wait())


main()
