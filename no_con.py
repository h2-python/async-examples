'''Run two coroutines'''
import asyncio

from util import delay


async def add_one(n: int) -> int:
    '''coroutine add_one'''
    return n + 1


async def hello() -> str:
    '''coroutine hello'''
    await delay(2)
    return "Hello"


async def main() -> None:
    '''coroutine main'''
    msg = await hello()
    result = await add_one(1)
    print(f"result:{result}")
    print(f'msg:{msg}')


if __name__ == '__main__':
    asyncio.run(main())
