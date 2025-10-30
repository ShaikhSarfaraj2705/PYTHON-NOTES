#Async IO:Asynchronous I/O,async for short,is a programming pattern that allows for high 
#performance I/O operations in a concurrent and non-bloking manner.in python,asyc programming
#is achieved through the use of the asyncio module and asynchronous functions.

import asyncio

async def  func1():
    await asyncio.sleep(1)
    return "Hello, async world"

async def main():
#     result=await func1()
#     print(result)



    L= await asyncio.gather(
        func1(),
        func1(),
        func1()
    )
    print(L)
asyncio.run(main())