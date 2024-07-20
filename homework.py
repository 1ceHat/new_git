from time import sleep, time
import asyncio


async def start_programm(name, power):
    print(f'Силач {name} начал соревнование')
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял шар номер {i+1}')

    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_programm('Я', 1))
    task2 = asyncio.create_task(start_programm('Он', 0.7))
    task3 = asyncio.create_task(start_programm('Она', 0.1))

    await task1
    await task2
    await task3


asyncio.run(start_tournament())

