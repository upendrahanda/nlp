import asyncio
import time

async def say_after(delay, what):
    """Coroutine that waits for a specified delay, then prints a message."""
    await asyncio.sleep(delay)
    print(what)

async def main():
    """Main coroutine that schedules and runs other coroutines."""
    print(f"started at {time.strftime('%X')}")

    # Create tasks to run concurrently.
    task1 = asyncio.create_task(say_after(2, 'hello'))
    task2 = asyncio.create_task(say_after(1, 'world'))

    # 'await' on the tasks to ensure they are both completed.
    # The program will run these concurrently, so the total time
    # will be close to the longest task (2 seconds).
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

if __name__ == "__main__":
    # This is the entry point for running the asyncio program.
    # It starts the event loop and runs the `main` coroutine.
    asyncio.run(main())