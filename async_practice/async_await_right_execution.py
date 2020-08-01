import asyncio
import time
"""
sleep function in normal and wrong are the "same". They "sleep" without allowing others to use the resources. Whereas this allows access to the resources when it is asleep.
In case 2(wrong) we added async to the normal function. However the event loop will run it without interruption. Why? Because we didn't tell where the loop is allowed to interrupt your function to run another task.

In case 3 we told the event loop exactly where to interrupt the function to run another task. Where exactly?
"""
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')