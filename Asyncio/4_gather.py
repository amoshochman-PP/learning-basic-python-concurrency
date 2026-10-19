import asyncio
from common import timer, asyncio_wait


async def loop_wait():
    function_calls = [asyncio_wait() for _ in range(5)]
    await asyncio.gather(*function_calls)


@timer
def main():
    asyncio.run(loop_wait())


main()
