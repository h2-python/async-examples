'''concurrent execution of long running tasks'''
import asyncio

from util import delay


async def main() -> None:
    '''long running'''
    sleep5 = asyncio.create_task(delay(5))
    sleep3 = asyncio.create_task(delay(3))
    sleep1 = asyncio.create_task(delay(1))

    await sleep5
    await sleep3
    await sleep1


asyncio.run(main())
