import asyncio

async def factorial(n):
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    return f

async def main():
    L = await asyncio.gather(factorial(2), factorial(3), factorial(4))
    print(L)  # [2, 6, 24]


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
