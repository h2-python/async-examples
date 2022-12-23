'''concurrent execution'''
import asyncio

from util import delay


async def main() -> None:
    '''coroutine main'''
    print()
    sleep_for_3sec = asyncio.create_task(delay(3))
    #print(f'sleep_for_3sec:{sleep_for_3sec}')
    print(f'type(sleep_for_3sec):{type(sleep_for_3sec)}')
    result = await sleep_for_3sec
    print(f'result:{result}')


if __name__ == '__main__':
    asyncio.run(main())
