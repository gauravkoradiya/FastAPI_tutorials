"""
https://stackoverflow.com/a/50758540/7786625

why do you need asyncio, not just plain code?
Answer is - asyncio allows you to get performance benefit when you parallelize I/O blocking operations (like reading/writing to network).


example that uses asyncio.sleep to imitate I/O blocking operation and asyncio.gather that shows how you can run multiple blocking operations concurrently:
"""

import asyncio
import time


async def io_related(name):
    print(f'{name} started')
    await asyncio.sleep(1)
    # time.sleep(1)
    print(f'{name} finished')


async def main():
    await asyncio.gather(
        io_related('first'),
        io_related('second'),
        io_related('Third'),
        io_related('Four'),
        io_related('Five'),
        io_related('Six'),
        io_related('Seven'),
        io_related('Eight'),
        io_related('Nine'),

    )


if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(main())
    print(f'{time.time()-start} second.')