'''asyncio example'''
import asyncio


async def delay(sec: int) -> int:
    '''async delay for sec second(s)'''
    print(f'\n--- Start pausing for {sec} second(s)')
    await asyncio.sleep(sec)
    print(f'--- Finish pausing for {sec} second(s)\n')
    return sec
