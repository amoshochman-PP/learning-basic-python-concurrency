import asyncio
from common import timer

NUMBER_OF_TASKS = 5


async def wait():
    await asyncio.sleep(1)
    print(f"Slept 1 sec")


async def loop_wait():
    for i in range(NUMBER_OF_TASKS):
        #await wait()
        asyncio.create_task(wait())

@timer
def main():
    asyncio.run(loop_wait())


main()
