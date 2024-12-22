import asyncio
from asyncio import Queue

def parse_input(input_string):
    return map(int, input_string.split(","))

async def writer(queue, delay, stop_event):
    count = 0
    await asyncio.sleep(delay)
    while not stop_event.is_set():
        await queue.put(f"{count}_{delay}")
        count += 1
        await asyncio.sleep(delay)

async def stacker(queue, stack, stop_event):
    while not stop_event.is_set():
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.1)
            stack.append(item)
        except asyncio.TimeoutError:
            pass

async def reader(stack, count, delay, stop_event):
    await asyncio.sleep(delay)
    for _ in range(count):
        while not stack:
            await asyncio.sleep(0.1)
        print(stack.pop(0))
    stop_event.set()

async def main():
    input_string = input()
    delay1, delay2, delay3, count = parse_input(input_string)

    queue = Queue()
    stack = []
    stop_event = asyncio.Event()

    writer1 = asyncio.create_task(writer(queue, delay1, stop_event))
    writer2 = asyncio.create_task(writer(queue, delay2, stop_event))
    stacker_task = asyncio.create_task(stacker(queue, stack, stop_event))
    reader_task = asyncio.create_task(reader(stack, count, delay3, stop_event))

    await reader_task

    writer1.cancel()
    writer2.cancel()
    stacker_task.cancel()

    await asyncio.gather(writer1, writer2, stacker_task, return_exceptions=True)

asyncio.run(main())
