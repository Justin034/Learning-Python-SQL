import asyncio

async def tryout():
    print("This will print out second")

async def main():
    print("start of main coroutine")
    task = tryout()
    task1 = asyncio.create_task(tryout())
    task2 = asyncio.create_task(tryout())
    print("Thus")
    temp = await task
    print("test1")
    temp1 = await task1
    print("test2")
    temp2 = await task2
    

asyncio.run(main())