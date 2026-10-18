import asyncio
from common import timer


async def wait(i):
    print(f"Sleeping: {i}")
    await asyncio.sleep(1)


async def loop_wait():
    function_calls = [wait(i) for i in range(5)]
    await asyncio.gather(*function_calls)


@timer
def main():
    asyncio.run(loop_wait())


main()
